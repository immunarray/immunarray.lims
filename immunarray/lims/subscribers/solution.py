# -*- coding: utf-8 -*-
from decimal import Decimal

from bika.lims.permissions import disallow_default_contenttypes
from immunarray.lims import logger
from immunarray.lims.interfaces.material import IMaterial
from immunarray.lims.interfaces.solution import ISolution
from immunarray.lims.permissions import AddSolution
from plone.api.content import find
from plone.api.portal import get_tool


def SolutionFTIModified(instance, event):
    """The ISolution behaviour has been applied to a Dexterity FTI!
    """
    if ISolution.__identifier__ in instance.behaviors:  # [american spelling]
        # Set some FTI fields to "Solution" defaults
        wf = get_tool("portal_workflow")
        wf._chains_by_type[instance.id] = ('solution_workflow',)
        instance.add_permission = 'immunarray.lims.permissions.AddSolution'
        instance.klass = 'immunarray.lims.content.solution.Solution'
        descr = instance.description if instance.description else instance.title
        descr = 'Solution: ' + descr.replace('Solution: ', '')
        instance.description = descr


def SolutionModified(instance, event):
    """A new solution has been created!
    """
    instance.manage_permission(AddSolution, [], 0)
    disallow_default_contenttypes(instance)
    UpdateSourceMaterials(instance, event)


def UpdateSourceMaterials(instance, event):
    """Update remaining material for anything that was used in the solution
    """
    mu = instance.materials_used
    if mu:
        for x in mu:  # {'material title (key)':'mass/volume'(value),}
            brains = find(object_provides=IMaterial.__identifier__, Title=x)
            if brains:
                material = brains[0].getObject()
                temp = Decimal(material.remaining_amount) - Decimal(mu[x])
                material.remaining_amount = float(temp)
            else:
                logger.warn(
                    "%s: Update source materials: material not found: %s" %
                    (instance, x))

    su = instance.solutions_used
    if su:
        for x in su:  # {'solution title (key)':'mass/volume'(value),}
            brains = find(object_provides=ISolution.__identifier__, Title=x)
            if brains:
                solution = brains[0].getObject()
                temp = Decimal(solution.remaining_amount) - Decimal(su[x])
                solution.remaining_amount = float(temp)
            else:
                logger.warn(
                    "%s: Update source materials: solution not found: %s" %
                    (instance, x))

# -*- coding: utf-8 -*-
from immunarray.lims.interfaces.solution import ISolution
from immunarray.lims.permissions import AddSolution
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

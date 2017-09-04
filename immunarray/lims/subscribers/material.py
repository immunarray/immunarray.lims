# -*- coding: utf-8 -*-
from bika.lims.permissions import disallow_default_contenttypes
from immunarray.lims.interfaces.material import IMaterial
from immunarray.lims.permissions import AddMaterial
from plone.api.portal import get_tool


def MaterialFTIModified(instance, event):
    """The IMaterial behaviour has been applied to a Dexterity FTI!
    """
    if IMaterial.__identifier__ in instance.behaviors:  # [american spelling]
        # Set some FTI fields to "Material" defaults
        wf = get_tool("portal_workflow")
        wf._chains_by_type[instance.id] = ('material_workflow',)
        instance.add_permission = 'immunarray.lims.permissions.AddMaterial'
        instance.klass = 'immunarray.lims.content.material.Material'
        descr = instance.description if instance.description else instance.title
        descr = 'Material: ' + descr.replace('Material: ', '')
        instance.description = descr


def MaterialModified(instance, event):
    """A new material has been created!
    """
    instance.manage_permission(AddMaterial, [], 0)
    disallow_default_contenttypes(instance)

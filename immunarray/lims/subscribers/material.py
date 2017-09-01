# -*- coding: utf-8 -*-
from immunarray.lims.interfaces.material import IMaterial
from immunarray.lims.permissions import AddMaterial


def MaterialFTIModified(instance, event):
    """The IMaterial behaviour has been applied to a Dexterity FTI!
    """
    if IMaterial.__identifier__ in instance.behaviors:  # [sic]
        # Set some FTI fields to "Material" defaults
        instance.add_permission = 'immunarray.lims.permissions.AddMaterial'
        instance.klass = 'immunarray.lims.content.material.Material'
        descr = instance.description if instance.description else instance.title
        descr = 'Material: ' + descr.replace('Material: ', '')
        instance.description = descr


def MaterialModified(instance, event):
    """A new material has been created!
    """
    instance.manage_permission(AddMaterial, [], 0)

# -*- coding: utf-8 -*-
from bika.lims.permissions import disallow_default_contenttypes
from immunarray.lims.interfaces.material import IMaterial
from immunarray.lims.permissions import AddMaterial, AddSite, AddProvider
from plone.api.portal import get_tool



def ProviderAdded(instance, event):
    """A new material has been created!
    """
    instance.manage_permission(AddProvider, [], 0)
    disallow_default_contenttypes(instance)

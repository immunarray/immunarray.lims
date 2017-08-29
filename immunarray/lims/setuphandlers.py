from Products.CMFCore.permissions import View, ListFolderContents, \
    AccessContentsInformation, ModifyPortalContent
from Products.CMFPlone import permissions
from Products.CMFPlone.interfaces import INonInstallable
from bika.lims.permissions import disallow_default_contenttypes
from immunarray.lims.permissions import setup_default_permissions, \
    AddAssayBillingRequest, AddBillingProgram
from plone.api.content import create
from plone.app.contenttypes import permissions
from zope.component.hooks import getSite
from zope.interface import implementer


@implementer(INonInstallable)
class HiddenProfiles(object):
    def getNonInstallableProfiles(self):
        """Hide bika.lims and our own uninstall profile from site-creation
        and quickinstaller
        """
        return [
            'bika.lims:default',
            'immunarray.lims:uninstall',
        ]


def setupVarious(context):
    if context.readDataFile('immunarraylims_default.txt') is None:
        return

    portal = getSite()

    remove_default_content(portal)

    setup_default_permissions(portal)
    make_billing(portal)


def remove_default_content(portal):
    del_ids = []
    for obj_id in ['Members', 'news', 'events']:
        if obj_id in portal.objectIds():
            del_ids.append(obj_id)
    if del_ids:
        portal.manage_delObjects(ids=del_ids)


def make_billing(portal):
    """LIMS root object has been created
    Here we will add the ImmunArray specific objects and configuration.
    """
    b1 = create(portal, 'Folder', 'billing', 'Billing')
    b2 = create(portal['billing'], 'Folder', 'assaybillingrequests',
                'Assay Billing Requests')
    b3 = create(portal['billing'], 'Folder', 'billingprograms',
                'Billing Programs')

    disallow_default_contenttypes(b1)
    disallow_default_contenttypes(b2)
    disallow_default_contenttypes(b3)

    b1.setLayout('folder_contents')
    b2.setLayout('folder_contents')
    b3.setLayout('folder_contents')

    # Remove option to add folder to structure locations
    b2.manage_permission(
        permissions.AddFolder, [], 0)
    b2.manage_permission(
        View, ['LabManager', 'BillingExec'], 0)
    b2.manage_permission(
        AccessContentsInformation, ['LabManager', 'BillingExec'], 0)
    b2.manage_permission(
        ListFolderContents, ['LabManager', 'BillingExec'], 0)
    b2.manage_permission(
        AddAssayBillingRequest, ['LabManager', 'BillingExec'], 0)
    b2.manage_permission(
        ModifyPortalContent, ['LabManager', 'BillingExec'], 0)
    b3.manage_permission(
        permissions.AddFolder, [], 0)
    b3.manage_permission(
        View, ['LabManager', 'BillingExec'], 0)
    b3.manage_permission(
        AccessContentsInformation, ['LabManager', 'BillingExec'], 0)
    b3.manage_permission(
        ListFolderContents, ['LabManager', 'BillingExec'], 0)
    b3.manage_permission(
        AddBillingProgram, ['LabManager', 'BillingExec'], 0)
    b3.manage_permission(
        ModifyPortalContent, ['LabManager', 'BillingExec'], 0)


def uninstall(context):
    """Uninstall script"""
    if context.readDataFile('immunarraylims_uninstall.txt') is None:
        return
    # Do something during the uninstallation of this package
    pass

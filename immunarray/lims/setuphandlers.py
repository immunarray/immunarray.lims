from Products.CMFCore.permissions import View, ListFolderContents, \
    AccessContentsInformation, ModifyPortalContent
from Products.CMFPlone import permissions
from Products.CMFPlone.interfaces import INonInstallable
from bika.lims.permissions import disallow_default_contenttypes, AddLIMSRoot
from immunarray.lims.permissions import setup_default_permissions, \
    AddAssayBillingRequest, AddBillingProgram, AddCustomerServiceCall
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
    make_customer_service(portal)
    make_executive(portal)


def remove_default_content(portal):
    del_ids = []
    for obj_id in ['Members', 'news', 'events']:
        if obj_id in portal.objectIds():
            del_ids.append(obj_id)
    if del_ids:
        portal.manage_delObjects(ids=del_ids)


def make_billing(portal):
    if 'billing' in portal:
        return

    b1 = create(portal, 'Folder', 'billing', 'Billing')
    b2 = create(b1, 'Folder', 'assaybillingrequests', 'Assay Billing Requests')
    b3 = create(b1, 'Folder', 'billingProgram_workflow', 'Billing Programs')

    disallow_default_contenttypes(b1)
    disallow_default_contenttypes(b2)
    disallow_default_contenttypes(b3)

    b1.setLayout('folder_contents')
    b2.setLayout('folder_contents')
    b3.setLayout('folder_contents')


    # @formatter:off
    b1.manage_permission(AddLIMSRoot, [], 0)
    b1.manage_permission(permissions.AddFolder, [], 0)
    b1.manage_permission(View, ['LabManager', 'BillingExec'], 0)
    b1.manage_permission(AccessContentsInformation, ['LabManager', 'BillingExec'], 0)
    b1.manage_permission(ListFolderContents, ['LabManager', 'BillingExec'], 0)
    b1.manage_permission(AddAssayBillingRequest, ['LabManager', 'BillingExec'], 0)
    b1.manage_permission(ModifyPortalContent, ['LabManager', 'BillingExec'], 0)

    b2.manage_permission(AddLIMSRoot, [], 0)
    b2.manage_permission(permissions.AddFolder, [], 0)
    b2.manage_permission(View, ['LabManager', 'BillingExec'], 0)
    b2.manage_permission(AccessContentsInformation, ['LabManager', 'BillingExec'], 0)
    b2.manage_permission(ListFolderContents, ['LabManager', 'BillingExec'], 0)
    b2.manage_permission(AddAssayBillingRequest, ['LabManager', 'BillingExec'], 0)
    b2.manage_permission(ModifyPortalContent, ['LabManager', 'BillingExec'], 0)

    b2.manage_permission(AddLIMSRoot, [], 0)
    b3.manage_permission(permissions.AddFolder, [], 0)
    b3.manage_permission(View, ['LabManager', 'BillingExec'], 0)
    b3.manage_permission(AccessContentsInformation, ['LabManager', 'BillingExec'], 0)
    b3.manage_permission(ListFolderContents, ['LabManager', 'BillingExec'], 0)
    b3.manage_permission(AddBillingProgram, ['LabManager', 'BillingExec'], 0)
    b3.manage_permission(ModifyPortalContent, ['LabManager', 'BillingExec'], 0)
    # @formatter:on


def make_customer_service(portal):
    if 'customerservice' in portal:
        return

    cs1 = create(portal, 'Folder', 'customerservice', 'Customer Service')
    cs2 = create(cs1, 'Folder', 'customercalls', 'Customer Calls')
    cs3 = create(cs1, 'Folder', 'providercalls', 'Provider Calls')

    disallow_default_contenttypes(cs1)
    disallow_default_contenttypes(cs2)
    disallow_default_contenttypes(cs3)

    cs1.setLayout('folder_contents')
    cs2.setLayout('folder_contents')
    cs3.setLayout('folder_contents')


    # @formatter:off
    cs1.manage_permission(AddLIMSRoot, [], 0)
    cs1.manage_permission(permissions.AddFolder, [], 0)
    cs1.manage_permission(View, ['LabManager', 'LabClerk', 'SalesRep', 'BillingExec'], 0)
    cs1.manage_permission(AccessContentsInformation, ['LabManager', 'LabClerk', 'SalesRep', 'BillingExec'], 0)
    cs1.manage_permission(ListFolderContents, ['LabManager', 'LabClerk', 'SalesRep', 'BillingExec'], 0)
    cs1.manage_permission(AddAssayBillingRequest, ['LabManager', 'LabClerk', 'SalesRep', 'BillingExec'], 0)
    cs1.manage_permission(ModifyPortalContent, ['LabManager', 'LabClerk', 'SalesRep', 'BillingExec'], 0)

    cs2.manage_permission(AddLIMSRoot, [], 0)
    cs2.manage_permission(permissions.AddFolder, [], 0)
    cs2.manage_permission(View, ['LabManager', 'LabClerk', 'SalesRep', 'BillingExec'], 0)
    cs2.manage_permission(AccessContentsInformation, ['LabManager', 'LabClerk', 'SalesRep', 'BillingExec'], 0)
    cs2.manage_permission(ListFolderContents, ['LabManager', 'LabClerk', 'SalesRep', 'BillingExec'], 0)
    cs2.manage_permission(AddCustomerServiceCall, ['LabManager', 'LabClerk', 'SalesRep', 'BillingExec'], 0)
    cs2.manage_permission(ModifyPortalContent, ['LabManager', 'LabClerk', 'SalesRep', 'BillingExec'], 0)

    cs3.manage_permission(AddLIMSRoot, [], 0)
    cs3.manage_permission(permissions.AddFolder, [], 0)
    cs3.manage_permission(View, ['LabManager', 'LabClerk', 'SalesRep', 'BillingExec'], 0)
    cs3.manage_permission(AccessContentsInformation, ['LabManager', 'LabClerk', 'SalesRep', 'BillingExec'], 0)
    cs3.manage_permission(ListFolderContents, ['LabManager', 'LabClerk', 'SalesRep', 'BillingExec'], 0)
    cs3.manage_permission(AddBillingProgram, ['LabManager', 'LabClerk', 'SalesRep', 'BillingExec'], 0)
    cs3.manage_permission(ModifyPortalContent, ['LabManager', 'LabClerk', 'SalesRep', 'BillingExec'], 0)
    # @formatter:on


def make_executive(portal):
    if 'executive' in portal:
        return

    ex1 = create(portal, 'Folder', 'executive', 'Executive')
    ex2 = create(ex1, 'Folder', 'reports', 'Reports')

    disallow_default_contenttypes(ex1)
    disallow_default_contenttypes(ex2)

    ex1.setLayout('folder_contents')
    ex2.setLayout('folder_contents')

    ex1.manage_permission(AddLIMSRoot, [], 0)

    ex1.manage_permission(
        permissions.AddFolder, [], 0)
    ex1.manage_permission(
        View, ['LabManager', 'Executive'], 0)
    ex1.manage_permission(
        AccessContentsInformation, ['LabManager', 'Executive'], 0)
    ex1.manage_permission(
        ListFolderContents, ['LabManager', 'Executive'], 0)
    ex1.manage_permission(
        ModifyPortalContent, ['LabManager', 'Executive'], 0)

    ex2.manage_permission(AddLIMSRoot, [], 0)
    ex2.manage_permission(
        permissions.AddFolder, [], 0)
    ex2.manage_permission(
        View, ['LabManager', 'Executive'], 0)
    ex2.manage_permission(
        AccessContentsInformation, ['LabManager', 'Executive'], 0)
    ex2.manage_permission(
        ListFolderContents, ['LabManager', 'Executive'], 0)
    ex2.manage_permission(
        ModifyPortalContent, ['LabManager', 'Executive'], 0)


def uninstall(context):
    """Uninstall script"""
    if context.readDataFile('immunarraylims_uninstall.txt') is None:
        return
    # Do something during the uninstallation of this package
    pass

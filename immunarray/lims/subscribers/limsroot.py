# -*- coding: utf-8 -*-
from pkg_resources import resource_filename
from plone import api
from plone.dexterity.fti import DexterityFTI
from zope.component.hooks import getSite
from Products.CMFCore.permissions import ModifyPortalContent
from plone.app.contenttypes import permissions
from Products.CMFCore.permissions import View, ListFolderContents, AccessContentsInformation, ModifyPortalContent


from immunarray.lims.permissions import AddMaterial, AddNCE, AddPatient, \
    AddProvider, AddPlate, AddSolution, AddiChipLot, AddiChipAssay, \
    AddCustomerServiceCall, AddRack, AddCommercialBox, \
    AddRandDBox, AddTestRun, AddNoFrameRun, AddEightFrameRun, AddThreeFrameRun, \
    AddClinicalAliquot, AddSite, AddClinicalSample, AddRandDSample, AddQCSample

from bika.lims.permissions import disallow_default_contenttypes

def get_schema_filename(folder, name):
    return resource_filename('immunarray.lims', '%s/%s.xml' % (folder, name))


def LIMSCreated(event):
    """LIMS root object has been created
    Here we will add the ImmunArray specific objects and configuration.
    """
    lims = event.lims
    portal = getSite()

    create_structure(lims)
    structure_permissions(lims)
    create_material_types(portal)
    create_solution_types(portal)


def create_structure(lims):
    for x in [
        [lims, 'Folder', 'materials', 'Materials'],
        [lims, 'Folder', 'solutions', 'Solutions'],
        [lims, 'Folder', 'ichiplots', 'iChip Lots'],
        [lims, 'Folder', 'testruns', 'Test Runs'],
        [lims, 'Folder', 'plates', 'Plates'],
        [lims, 'Folder', 'nce', 'Non Conformance Events'],
        [lims, 'Folder', 'inventory', 'Inventory'],
        [lims, 'Folder', 'patients', 'Patients'],
        [lims, 'Folder', 'providers', 'Providers'],
        [lims, 'Folder', 'ichipassay', 'iChip Assays'],
        [lims, 'Folder', 'customerservicecall', 'Customer Service Calls']
    ]:
        obj = api.content.create(container=x[0], type=x[1], id=x[2], title=x[3])
        obj.setLayout('folder_contents')
        disallow_default_contenttypes(obj)

        # Configuration to bottom of nav.
        lims.moveObjectsToBottom(['configuration'])


def structure_permissions(lims):
    # Remove option to add folder to structure locations
    lims.customerservicecall.manage_permission(permissions.AddFolder, [], 0)
    lims.ichipassay.manage_permission(permissions.AddFolder, [], 0)
    lims.ichiplots.manage_permission(permissions.AddFolder, [], 0)
    lims.inventory.manage_permission(permissions.AddFolder, [], 0)
    lims.materials.manage_permission(permissions.AddFolder, [], 0)
    lims.nce.manage_permission(permissions.AddFolder, [], 0)
    lims.patients.manage_permission(permissions.AddFolder, [], 0)
    lims.plates.manage_permission(permissions.AddFolder, [], 0)
    lims.providers.manage_permission(permissions.AddFolder, [], 0)
    lims.samples.manage_permission(permissions.AddFolder, [], 0)
    lims.sites.manage_permission(permissions.AddFolder, [], 0)
    lims.solutions.manage_permission(permissions.AddFolder, [], 0)
    lims.testruns.manage_permission(permissions.AddFolder, [], 0)

    # View permission
    lims.customerservicecall.manage_permission(View, ['LabManager','LabClerk','SalesRep','BillingExec'], 0)
    lims.ichipassay.manage_permission(View, ['LabManager','LabClerk'], 0)
    lims.ichiplots.manage_permission(View, ['LabManager','LabClerk'], 0)
    lims.inventory.manage_permission(View, ['LabManager','LabClerk','RandDManager','RandDLabClerk'], 0)
    lims.materials.manage_permission(View, ['LabManager','LabClerk','RandDManager','RandDLabClerk'], 0)
    lims.nce.manage_permission(View, ['LabManager', 'LabClerk', 'RandDManager', 'RandDLabClerk', 'RandDAnalyst', 'Executive', 'SalesRep', 'BillingExec'], 0)
    lims.patients.manage_permission(View, ['LabManager','LabClerk'], 0)
    lims.plates.manage_permission(View, ['LabManager','LabClerk','RandDManager','RandDLabClerk'], 0)
    lims.providers.manage_permission(View, ['LabManager','LabClerk','SalesRep'], 0)
    lims.sites.manage_permission(View, ['LabManager','LabClerk','SalesRep'], 0)
    lims.solutions.manage_permission(View, ['LabManager','LabClerk','RandDManager','RandDLabClerk'], 0)
    lims.testruns.manage_permission(View, ['LabManager','LabClerk'], 0)
    # Access Contents Information
    lims.customerservicecall.manage_permission(AccessContentsInformation, ['LabManager','LabClerk','SalesRep','BillingExec'], 0)
    lims.ichipassay.manage_permission(AccessContentsInformation, ['LabManager','LabClerk'], 0)
    lims.ichiplots.manage_permission(AccessContentsInformation, ['LabManager','LabClerk'], 0)
    lims.inventory.manage_permission(AccessContentsInformation, ['LabManager','LabClerk','RandDManager','RandDLabClerk'], 0)
    lims.materials.manage_permission(AccessContentsInformation, ['LabManager','LabClerk','RandDManager','RandDLabClerk'], 0)
    lims.nce.manage_permission(AccessContentsInformation, ['LabManager', 'LabClerk', 'RandDManager', 'RandDLabClerk', 'RandDAnalyst', 'Executive', 'SalesRep', 'BillingExec'], 0)
    lims.patients.manage_permission(AccessContentsInformation, ['LabManager','LabClerk'], 0)
    lims.plates.manage_permission(AccessContentsInformation, ['LabManager','LabClerk','RandDManager','RandDLabClerk'], 0)
    lims.providers.manage_permission(AccessContentsInformation, ['LabManager','LabClerk','SalesRep'], 0)
    lims.samples.manage_permission(AccessContentsInformation, ['LabManager','LabClerk','RandDManager','RandDLabClerk'], 0)
    lims.sites.manage_permission(AccessContentsInformation, ['LabManager','LabClerk','SalesRep'], 0)
    lims.solutions.manage_permission(AccessContentsInformation, ['LabManager','LabClerk','RandDManager','RandDLabClerk'], 0)
    lims.testruns.manage_permission(AccessContentsInformation, ['LabManager','LabClerk'], 0)
    # List Folder Contents
    lims.customerservicecall.manage_permission(ListFolderContents, ['LabManager','LabClerk','SalesRep','BillingExec'], 0)
    lims.ichipassay.manage_permission(ListFolderContents, ['LabManager','LabClerk'], 0)
    lims.ichiplots.manage_permission(ListFolderContents, ['LabManager','LabClerk'], 0)
    lims.inventory.manage_permission(ListFolderContents, ['LabManager','LabClerk','RandDManager','RandDLabClerk'], 0)
    lims.materials.manage_permission(ListFolderContents, ['LabManager','LabClerk','RandDManager','RandDLabClerk'], 0)
    lims.nce.manage_permission(ListFolderContents, ['LabManager', 'LabClerk', 'RandDManager', 'RandDLabClerk', 'RandDAnalyst', 'Executive', 'SalesRep', 'BillingExec'], 0)
    lims.patients.manage_permission(ListFolderContents, ['LabManager','LabClerk'], 0)
    lims.plates.manage_permission(ListFolderContents, ['LabManager','LabClerk','RandDManager','RandDLabClerk'], 0)
    lims.providers.manage_permission(ListFolderContents, ['LabManager','LabClerk','SalesRep'], 0)
    lims.samples.manage_permission(ListFolderContents, ['LabManager','LabClerk','RandDManager','RandDLabClerk'], 0)
    lims.sites.manage_permission(ListFolderContents, ['LabManager','LabClerk','SalesRep'], 0)
    lims.solutions.manage_permission(ListFolderContents, ['LabManager','LabClerk','RandDManager','RandDLabClerk'], 0)
    lims.testruns.manage_permission(ListFolderContents, ['LabManager','LabClerk'], 0)

    # Custom Add Permission
    lims.customerservicecall.manage_permission(AddCustomerServiceCall, ['LabManager','LabClerk','SalesRep','BillingExec'], 0)
    lims.ichipassay.manage_permission(AddiChipAssay, ['LabManager'], 0)
    lims.ichiplots.manage_permission(AddiChipLot, ['LabManager','LabClerk'], 0)
    lims.inventory.manage_permission(AddRack, ['LabManager','LabClerk','RandDManager','RandDLabClerk'], 0)
    lims.materials.manage_permission(AddMaterial, ['LabManager','LabClerk','RandDManager','RandDLabClerk'], 0)
    lims.nce.manage_permission(AddNCE, ['LabManager', 'LabClerk', 'RandDManager', 'RandDLabClerk', 'RandDAnalyst', 'Executive', 'SalesRep', 'BillingExec'], 0)
    lims.patients.manage_permission(AddPatient, ['LabManager','LabClerk'], 0)
    lims.plates.manage_permission(AddPlate, ['LabManager','LabClerk','RandDManager','RandDLabClerk'], 0)
    lims.providers.manage_permission(AddProvider, ['LabManager','LabClerk','SalesRep'], 0)
    lims.providers.manage_permission(AddClinicalSample, ['LabManager','LabClerk','RandDManager','RandDLabClerk'], 0)
    lims.providers.manage_permission(AddRandDSample, ['LabManager','LabClerk','RandDManager','RandDLabClerk'], 0)
    lims.providers.manage_permission(AddQCSample, ['LabManager','LabClerk','RandDManager','RandDLabClerk'], 0)
    lims.sites.manage_permission(AddSite, ['LabManager','LabClerk','SalesRep'], 0)
    lims.solutions.manage_permission(AddSolution, ['LabManager','LabClerk','RandDManager','RandDLabClerk'], 0)
    lims.testruns.manage_permission(AddEightFrameRun, ['LabManager','LabClerk'], 0)
    lims.testruns.manage_permission(AddNoFrameRun, ['LabManager','LabClerk'], 0)
    lims.testruns.manage_permission(AddTestRun, ['LabManager','LabClerk'], 0)
    lims.testruns.manage_permission(AddThreeFrameRun, ['LabManager','LabClerk'], 0)
    # Modify portal content
    lims.customerservicecall.manage_permission(ModifyPortalContent, ['LabManager'], 0)
    lims.ichipassay.manage_permission(ModifyPortalContent, ['LabManager'], 0)
    lims.ichiplots.manage_permission(ModifyPortalContent, ['LabManager'], 0)
    lims.inventory.manage_permission(ModifyPortalContent, ['LabManager'], 0)
    lims.materials.manage_permission(ModifyPortalContent, ['LabManager'], 0)
    lims.nce.manage_permission(ModifyPortalContent, ['LabManager'], 0)
    lims.patients.manage_permission(ModifyPortalContent, ['LabManager'], 0)
    lims.plates.manage_permission(ModifyPortalContent, ['LabManager'], 0)
    lims.providers.manage_permission(ModifyPortalContent, ['LabManager','LabClerk','SalesRep'], 0)
    lims.samples.manage_permission(ModifyPortalContent, ['LabManager'], 0)
    lims.sites.manage_permission(ModifyPortalContent, ['LabManager','LabClerk','SalesRep'], 0)
    lims.solutions.manage_permission(ModifyPortalContent, ['LabManager'], 0)
    lims.testruns.manage_permission(ModifyPortalContent, ['Manager'], 0)



def create_material_types(portal):
    materials = [
        ("caseinsalt", u"Casein Salt"),
        ("ethylalcohol", u"Ethyl Alcohol Denatured"),
        ("glycerol", u"Glycerol"),
        ("nacl", u"Sodium Chloride (NaCl)"),
        ("kcl", u"Potassium Chloride (KCl)"),
        ("kh2po4", u"Potassium Phosphatemonobasic (KH2PO4)"),
        ("na2hpo4", u"Sodium Phosphatedibasic (Na2HPO4)"),
        ("naoh", u"Sodium Hydroxide 2.5N (NaOH)"),
        ("tween20", u"Tween 20"),
        ("hcl37", u"Hydrochloricacid 37%"),
        ("iggcy3", u"IgG-Cy3"),
        ("igmaf647", u"IgM-AF647"),
    ]
    for tid, title in materials:
        fti = DexterityFTI(tid)
        fti.manage_changeProperties(
            factory=tid,
            title=title.encode('utf8'),
            description=u"Material: {0}".format(title.encode()),
            i18n_domain='immunarray.lims',
            klass='immunarray.lims.content.material.Material',
            model_file=get_schema_filename('materials', tid),
            immediate_view='view',
            icon_expr='string:document_icon.png',
            filter_content_types=True,
            allowed_content_types=[],
            global_allow=True,
            schema="immunarray.lims.interfaces.material.IMaterial",
            behaviors=[],
            add_permission='immunarray.lims.permissions.AddMaterial',
        )
        if tid in portal.portal_types:
            del portal.portal_types[tid]
        portal.portal_types._setObject(tid, fti)


def create_solution_types(portal):
    solutions = [
        ("1xpbs", u"PBS (1X)"),
        ("10xpbs", u"PBS (10X)"),
        ("1percentcasein", u"1% Casein in PBS"),
        ("70percentethanol", u"70% Ethanol (Cleaning Solution)"),
        ("tween22_4percentinpbs", u"22.4% Tween in PBS"),
        ("50percentglycerol", u"50% Glycerol"),
        ("10percenthcl", u"10% HCl"),
        ("3mkcl", u"3M KCl"),
        ("1mgpermligm_af647", u"1 mg/mL IgM-AF647"),
        ("1mgpermligg_cy3", u"1 mg/mL IgG-Cy3"),
    ]
    for tid, title in solutions:
        fti = DexterityFTI(tid)
        fti.manage_changeProperties(
            factory=tid,
            title=title.encode('utf8'),
            description=u"Solution: {0}".format(title.encode()),
            i18n_domain='immunarray.lims',
            klass='immunarray.lims.content.solution.Solution',
            model_file=get_schema_filename('solutions', tid),
            immediate_view='view',
            icon_expr='string:document_icon.png',
            filter_content_types=True,
            allowed_content_types=[],
            global_allow=True,
            schema="immunarray.lims.interfaces.solution.ISolution",
            behaviors=[],
            add_permission='immunarray.lims.permissions.AddSolution',
        )
        if tid in portal.portal_types:
            del portal.portal_types[tid]
        portal.portal_types._setObject(tid, fti)

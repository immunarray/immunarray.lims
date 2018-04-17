# -*- coding: utf-8 -*-
from AccessControl.Permissions import delete_objects, copy_or_move
from Products.CMFCore.permissions import AccessContentsInformation, \
    ListFolderContents, ModifyPortalContent, View
from bika.lims.permissions import AddLIMSRoot, disallow_default_contenttypes
from immunarray.lims.interfaces import IConfiguration, IInventory, IMaterials, \
    INonConformanceEvents, IPatients, IProviders, ISamples, ISites, \
    ISolutions, ITestRuns, IiChipAssays, IiChipLots
from immunarray.lims.permissions import AddClinicalSample, AddMaterial, \
    AddNCE, AddPatient, AddProvider, AddQCSample, AddRack, \
    AddRandDSample, AddSite, AddSolution, AddTestRun, AddThreeFrameRun, \
    AddiChipAssay, AddiChipLot
from pkg_resources import resource_filename
from plone.api.content import create
from plone.app.contenttypes import permissions
from zope.interface import alsoProvides


def get_schema_filename(folder, name):
    return resource_filename('immunarray.lims', '%s/%s.xml' % (folder, name))


def LIMSCreated(event):
    """LIMS root object has been created
    Here we will add the ImmunArray specific objects and configuration.
    """
    lims = event.lims

    create_structure(lims)
    structure_permissions(lims)


def create_structure(lims):
    for x in [
        [lims, 'Folder', 'sites', 'Sites', ISites],
        [lims, 'Folder', 'samples', 'Samples', ISamples],
        [lims, 'Folder', 'materials', 'Materials', IMaterials],
        [lims, 'Folder', 'solutions', 'Solutions', ISolutions],
        [lims, 'Folder', 'ichiplots', 'iChip Lots', IiChipLots],
        [lims, 'Folder', 'testruns', 'Test Runs', ITestRuns],
        [lims, 'Folder', 'nce', 'Non Conformance Events', INonConformanceEvents],
        [lims, 'Folder', 'inventory', 'Inventory', IInventory],
        [lims, 'Folder', 'patients', 'Patients', IPatients],
        [lims, 'Folder', 'providers', 'Providers', IProviders],
        [lims, 'Folder', 'ichipassay', 'iChip Assays', IiChipAssays],
        [lims, 'Folder', 'configuration', 'Configuration', IConfiguration],
    ]:
        obj = create(container=x[0], type=x[1], id=x[2], title=x[3])
        obj.setLayout('folder_contents')
        disallow_default_contenttypes(obj)
        alsoProvides(obj, x[4])

    # Create configuration after other stuff, so that it's at the bottom of nav
    configuration = lims.configuration
    for x in [
        [configuration, 'Folder', 'aliquoting', 'Aliquoting'],
        [configuration, 'Folder', 'departments', 'Departments'],
        [configuration, 'Folder', 'contacts', 'Contacts'],
        [configuration, 'Folder', 'samplepoints', 'Sample Points'],
        [configuration, 'Folder', 'sampletypes', 'Sample Types'],
        [configuration, 'Folder', 'analysisservices', 'Analysis Services'],
        [configuration, 'Folder', 'calculations', 'Calculations'],
    ]:
        instance = create(container=x[0], type=x[1], id=x[2], title=x[3])
        instance.setLayout('folder_contents')
        disallow_default_contenttypes(instance)


def structure_permissions(lims):
    # @formatter:off

    # Prevent anyone from adding a LIMSRoot inside of a LIMSRoot Allow for
    # all users to see folder
    lims.manage_permission(AddLIMSRoot, [], 0)
    lims.manage_permission(ListFolderContents, ['Manager', 'LabManager', 'LabClerk', 'Owner', 'Administrator', 'Member', 'RandDLabClerk', 'RandDLabManager'], 0)
    lims.manage_permission(View, ['Manager', 'LabManager', 'LabClerk', 'Owner', 'Administrator', 'Member', 'RandDLabClerk', 'RandDLabManager'], 0)
    lims.manage_permission(delete_objects, [], 0)

    # Delete
    lims.ichipassay.manage_permission(delete_objects, [], 0)
    lims.ichiplots.manage_permission(delete_objects, [], 0)
    lims.inventory.manage_permission(delete_objects, [], 0)
    lims.materials.manage_permission(delete_objects, [], 0)
    lims.nce.manage_permission(delete_objects, [], 0)
    lims.patients.manage_permission(delete_objects, [], 0)
    lims.providers.manage_permission(delete_objects, [], 0)
    lims.samples.manage_permission(delete_objects, [], 0)
    lims.sites.manage_permission(delete_objects, [], 0)
    lims.solutions.manage_permission(delete_objects, [], 0)
    lims.testruns.manage_permission(delete_objects, [], 0)

    # Remove option to add folder to structure locations
    lims.ichipassay.manage_permission(permissions.AddFolder, [], 0)
    lims.ichiplots.manage_permission(permissions.AddFolder, [], 0)
    lims.inventory.manage_permission(permissions.AddFolder, [], 0)
    lims.materials.manage_permission(permissions.AddFolder, [], 0)
    lims.nce.manage_permission(permissions.AddFolder, [], 0)
    lims.patients.manage_permission(permissions.AddFolder, [], 0)
    lims.providers.manage_permission(permissions.AddFolder, [], 0)
    lims.samples.manage_permission(permissions.AddFolder, [], 0)
    lims.sites.manage_permission(permissions.AddFolder, [], 0)
    lims.solutions.manage_permission(permissions.AddFolder, [], 0)
    lims.testruns.manage_permission(permissions.AddFolder, [], 0)

    # View permission
    lims.ichipassay.manage_permission(View, ['LabManager', 'LabClerk'], 0)
    lims.ichiplots.manage_permission(View, ['LabManager', 'LabClerk'], 0)
    lims.inventory.manage_permission(View, ['LabManager', 'LabClerk', 'RandDManager', 'RandDLabClerk'], 0)
    lims.materials.manage_permission(View, ['LabManager', 'LabClerk', 'RandDManager', 'RandDLabClerk'], 0)
    lims.nce.manage_permission(View, ['LabManager', 'LabClerk', 'RandDManager', 'RandDLabClerk', 'RandDAnalyst', 'Executive', 'SalesRep', 'BillingExec'], 0)
    lims.patients.manage_permission(View, ['LabManager', 'LabClerk'], 0)
    lims.providers.manage_permission(View, ['LabManager', 'LabClerk', 'SalesRep'], 0)
    lims.sites.manage_permission(View, ['LabManager', 'LabClerk', 'SalesRep'], 0)
    lims.solutions.manage_permission(View, ['LabManager', 'LabClerk', 'RandDManager', 'RandDLabClerk'], 0)
    lims.testruns.manage_permission(View, ['LabManager', 'LabClerk'], 0)
    lims.samples.manage_permission(View, ['LabManager', 'LabClerk', 'RandDManager', 'RandDLabClerk'], 0)

    # Access Contents Information
    lims.ichipassay.manage_permission(AccessContentsInformation, ['LabManager', 'LabClerk'], 0)
    lims.ichiplots.manage_permission(AccessContentsInformation, ['LabManager', 'LabClerk'], 0)
    lims.inventory.manage_permission(AccessContentsInformation, ['LabManager', 'LabClerk', 'RandDManager', 'RandDLabClerk'], 0)
    lims.materials.manage_permission(AccessContentsInformation, ['LabManager', 'LabClerk', 'RandDManager', 'RandDLabClerk'], 0)
    lims.nce.manage_permission(AccessContentsInformation, ['LabManager', 'LabClerk', 'RandDManager', 'RandDLabClerk', 'RandDAnalyst', 'Executive', 'SalesRep', 'BillingExec'], 0)
    lims.patients.manage_permission(AccessContentsInformation, ['LabManager', 'LabClerk'], 0)
    lims.providers.manage_permission(AccessContentsInformation, ['LabManager', 'LabClerk', 'SalesRep'], 0)
    lims.samples.manage_permission(AccessContentsInformation, ['LabManager', 'LabClerk', 'RandDManager', 'RandDLabClerk'], 0)
    lims.sites.manage_permission(AccessContentsInformation, ['LabManager', 'LabClerk', 'SalesRep'], 0)
    lims.solutions.manage_permission(AccessContentsInformation, ['LabManager', 'LabClerk', 'RandDManager', 'RandDLabClerk'], 0)
    lims.testruns.manage_permission(AccessContentsInformation, ['LabManager', 'LabClerk'], 0)

    # List Folder Contents
    lims.ichipassay.manage_permission(ListFolderContents, ['LabManager', 'LabClerk'], 0)
    lims.ichiplots.manage_permission(ListFolderContents, ['LabManager', 'LabClerk'], 0)
    lims.inventory.manage_permission(ListFolderContents, ['LabManager', 'LabClerk', 'RandDManager', 'RandDLabClerk'], 0)
    lims.materials.manage_permission(ListFolderContents, ['LabManager', 'LabClerk', 'RandDManager', 'RandDLabClerk'], 0)
    lims.nce.manage_permission(ListFolderContents, ['LabManager', 'LabClerk', 'RandDManager', 'RandDLabClerk', 'RandDAnalyst', 'Executive', 'SalesRep', 'BillingExec'], 0)
    lims.patients.manage_permission(ListFolderContents, ['LabManager', 'LabClerk'], 0)
    lims.providers.manage_permission(ListFolderContents, ['LabManager', 'LabClerk', 'SalesRep'], 0)
    lims.samples.manage_permission(ListFolderContents, ['LabManager', 'LabClerk', 'RandDManager', 'RandDLabClerk'], 0)
    lims.sites.manage_permission(ListFolderContents, ['LabManager', 'LabClerk', 'SalesRep'], 0)
    lims.solutions.manage_permission(ListFolderContents, ['LabManager', 'LabClerk', 'RandDManager', 'RandDLabClerk'], 0)
    lims.testruns.manage_permission(ListFolderContents, ['LabManager', 'LabClerk'], 0)

    # Custom Add Permissions
    # Include copy_or_move, it's required to insert new content.
    import pdb
    pdb.set_trace()
    pass
    lims.ichipassay.manage_permission(AddiChipAssay, ['LabManager'], 0)
    lims.ichipassay.manage_permission(copy_or_move, ['LabManager'], 0)
    lims.ichiplots.manage_permission(AddiChipLot, ['LabManager', 'LabClerk'], 0)
    lims.ichiplots.manage_permission(copy_or_move, ['LabManager', 'LabClerk'], 0)
    lims.inventory.manage_permission(AddRack, ['LabManager', 'LabClerk', 'RandDManager', 'RandDLabClerk'], 0)
    lims.inventory.manage_permission(copy_or_move, ['LabManager'], 0)
    lims.materials.manage_permission(AddMaterial, ['LabManager', 'LabClerk', 'RandDManager', 'RandDLabClerk'], 0)
    lims.materials.manage_permission(copy_or_move, ['LabManager', 'LabClerk', 'RandDManager', 'RandDLabClerk'], 0)
    lims.nce.manage_permission(AddNCE, ['LabManager', 'LabClerk', 'RandDManager', 'RandDLabClerk', 'RandDAnalyst', 'Executive', 'SalesRep', 'BillingExec'], 0)
    lims.nce.manage_permission(copy_or_move, ['LabManager', 'LabClerk', 'RandDManager', 'RandDLabClerk', 'RandDAnalyst', 'Executive', 'SalesRep', 'BillingExec'], 0)
    lims.patients.manage_permission(AddPatient, ['LabManager', 'LabClerk'], 0)
    lims.patients.manage_permission(copy_or_move, ['LabManager', 'LabClerk'], 0)
    lims.providers.manage_permission(AddProvider, ['LabManager', 'LabClerk', 'SalesRep'], 0)
    lims.providers.manage_permission(copy_or_move, ['LabManager', 'LabClerk', 'SalesRep'], 0)
    lims.sites.manage_permission(AddSite, ['LabManager', 'LabClerk', 'SalesRep'], 0)
    lims.sites.manage_permission(copy_or_move, ['LabManager', 'LabClerk', 'SalesRep'], 0)
    lims.solutions.manage_permission(AddSolution, ['LabManager', 'LabClerk', 'RandDManager', 'RandDLabClerk'], 0)
    lims.solutions.manage_permission(copy_or_move, ['LabManager', 'LabClerk', 'RandDManager', 'RandDLabClerk'], 0)
    lims.testruns.manage_permission(copy_or_move, ['LabManager', 'LabClerk'], 0)
    lims.testruns.manage_permission(AddThreeFrameRun, ['LabManager', 'LabClerk'], 0)
    lims.testruns.manage_permission(copy_or_move, ['LabManager', 'LabClerk'], 0)
    lims.testruns.manage_permission(AddTestRun, ['LabManager', 'LabClerk'], 0)
    lims.testruns.manage_permission(copy_or_move, ['LabManager', 'LabClerk'], 0)
    lims.samples.manage_permission(AddClinicalSample, ['LabManager', 'LabClerk'], 0)
    lims.samples.manage_permission(copy_or_move, ['LabManager', 'LabClerk'], 0)
    lims.samples.manage_permission(AddRandDSample, ['LabManager', 'LabClerk', 'RandDManager', 'RandDLabClerk'], 0)
    lims.samples.manage_permission(copy_or_move, ['LabManager', 'LabClerk', 'RandDManager', 'RandDLabClerk'], 0)
    lims.samples.manage_permission(AddQCSample, ['LabManager', 'LabClerk'], 0)
    lims.samples.manage_permission(copy_or_move, ['LabManager', 'LabClerk'], 0)

    # Modify portal content
    lims.ichipassay.manage_permission(ModifyPortalContent, ['LabManager'], 0)
    lims.ichiplots.manage_permission(ModifyPortalContent, ['LabManager'], 0)
    lims.inventory.manage_permission(ModifyPortalContent, ['LabManager'], 0)
    lims.materials.manage_permission(ModifyPortalContent, ['LabManager'], 0)
    lims.nce.manage_permission(ModifyPortalContent, ['LabManager'], 0)
    lims.patients.manage_permission(ModifyPortalContent, ['LabManager'], 0)
    lims.providers.manage_permission(ModifyPortalContent, ['LabManager', 'LabClerk', 'SalesRep'], 0)
    lims.sites.manage_permission(ModifyPortalContent, ['LabManager', 'LabClerk', 'SalesRep'], 0)
    lims.solutions.manage_permission(ModifyPortalContent, ['LabManager'], 0)
    lims.testruns.manage_permission(ModifyPortalContent, ['LabManager', 'LabClerk'], 0)
    lims.samples.manage_permission(ModifyPortalContent, ['LabManager', 'LabClerk'], 0)
    lims.samples.manage_permission(ModifyPortalContent, ['LabManager', 'LabClerk', 'RandDManager', 'RandDLabClerk'], 0)
    lims.samples.manage_permission(ModifyPortalContent, ['LabManager', 'LabClerk'], 0)
    # @formatter:on

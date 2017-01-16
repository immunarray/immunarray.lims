from plone.registry.interfaces import IRegistry
from Products.CMFPlone.interfaces import INavigationSchema
from Products.CMFPlone.interfaces import INonInstallable
from zope.component import getUtility
from zope.component.hooks import getSite
from zope.interface import implementer

from immunarray.lims.permissions import *

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
    mp = portal.manage_permission
    mp(AddMaterial, [], 0)
    mp(AddSolution, [], 0)
    mp(AddiChipLot, [], 0)
    mp(AddiChip, [], 0)
    mp(AddWorklist, [], 0)
    mp(AddPlate, [], 0)
    mp(AddNCE, [], 0)
    mp(AddPatient, [], 0)
    mp(AddProvider, [], 0)
    mp(AddClinicalSample, [], 0)
    mp(AddiChipAssay, [], 0)
    mp(AddCustomerServiceCall, [], 0)

def uninstall(context):
    """Uninstall script"""
    if context.readDataFile('immunarraylims_uninstall.txt') is None:
        return
    # Do something during the uninstallation of this package
    pass

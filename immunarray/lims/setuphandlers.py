from Products.CMFPlone.interfaces import INavigationSchema
from plone.registry.interfaces import IRegistry
from zope.component import getUtility

from immunarray.lims.permissions import *
from zope.component.hooks import getSite

def setupVarious(context):
    if context.readDataFile('immunarray.lims.txt') is None:
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

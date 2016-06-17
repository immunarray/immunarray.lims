from immunarray.lims.permissions import *


def setupVarious(context):
    if context.readDataFile('immunarray.lims.txt') is None:
        return
    portal = context.getSite()

    mp = portal.materials.manage_permission
    mp(AddMaterial, ['Manager', 'Owner'], 0)

    mp = portal.solutions.manage_permission
    mp(AddSolution, ['Manager', 'Owner'], 0)

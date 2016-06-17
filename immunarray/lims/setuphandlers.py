from immunarray.lims.permissions import *


def setupVarious(context):
    if context.readDataFile('immunarray.lims.txt') is None:
        return
    portal = context.getSite()

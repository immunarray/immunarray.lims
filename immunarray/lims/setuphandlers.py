from Products.CMFCore.utils import getToolByName

def setupVarious(context):
    """Initial configuration not handled by generic setup
    """

    if context.readDataFile('immunarray.lims.txt') is None:
        return

    portal = context.getSite()

    # objects created from profiles/structure are not initially indexed
    # All objects in structure/.objects should be entered here.
    for obj_id in ('ichiplots',):
        obj = portal._getOb(obj_id)
        obj.reindexObject()

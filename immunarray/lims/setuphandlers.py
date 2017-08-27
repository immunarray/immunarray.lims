from Products.CMFPlone.interfaces import INonInstallable
from immunarray.lims.permissions import setup_default_permissions
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


def remove_default_content(portal):
    del_ids = []
    for obj_id in ['Members', 'news', 'events']:
        if obj_id in portal.objectIds():
            del_ids.append(obj_id)
    if del_ids:
        portal.manage_delObjects(ids=del_ids)


def uninstall(context):
    """Uninstall script"""
    if context.readDataFile('immunarraylims_uninstall.txt') is None:
        return
    # Do something during the uninstallation of this package
    pass

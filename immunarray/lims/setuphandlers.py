# -*- coding: utf-8 -*-

from immunarray.lims.permissions import AddMaterial

from immunarray.lims import messageFactory as _
from plone import api
from plone.app.dexterity import MessageFactory as _
from plone.dexterity.fti import DexterityFTI
from zope.lifecycleevent import modified


def setupMaterials(context):
    if context.readDataFile('immunarray.lims.txt') is None:
        return

    portal = context.getSite()

    # Create initial /materials folder if it doesn't yet exist
    if 'materials' not in portal:
        api.content.create(container=portal,
                           id='materials',
                           type='Folder',
                           title='Materials')
        modified(portal.materials)

    # built-in materials
    materials = [
        ('caseinsalt', _(u"Casein Salt"),
         """<model xmlns="http://namespaces.plone.org/supermodel/schema"><schema>
         </schema></model>"""),
        ('ethylalcoholdenatured', _(u"Ethylalcahol Denatured"),
         """<model xmlns="http://namespaces.plone.org/supermodel/schema"><schema>
         </schema></model>"""),
        ('glycerol', _(u"Glycerol"),
         """<model xmlns="http://namespaces.plone.org/supermodel/schema"><schema>
         </schema></model>"""),
        ('kcl', _(u"Potassium Chloride (KCl)"),
         """<model xmlns="http://namespaces.plone.org/supermodel/schema"><schema>
         </schema></model>"""),
        ('kcl', _(u"Potassium Chloride (KCl)"),
         """<model xmlns="http://namespaces.plone.org/supermodel/schema"><schema>
         </schema></model>"""),
        ('kh2po4', _(u"Potassium Phosphatemonobasic (KH2PO4)"),
         """<model xmlns="http://namespaces.plone.org/supermodel/schema"><schema>
         </schema></model>"""),
    ]

    for id, title, schema in materials:
        fti = DexterityFTI(id)
        fti.id = id

        fti.manage_changeProperties(
            factory=id,
            title=title.encode('utf8'),
            description=u"Material FTI for %s" % title.encode(),
            i18n_domain='immunarray.lims',
            klass='immunarray.lims.interfaces.IMaterial',
            model_source=schema,
            icon_expr=portal.absolute_url() + '/document_icon.png',
            add_view_expr=portal.materials.absolute_url() + '++add+' + id,
            filter_content_types=True,
            allowed_content_types=[],
            model_file=None,
            global_allow=True,
            behaviors=[
                "immunarray.lims.interfaces.material.IMaterial",
                "plone.app.dexterity.behaviors.metadata.IDublinCore"
            ],
            default_view_fallback=False,
            immediate_view='view',
            default_view='view',
            view_methods=['view', ],
            add_permission='immunarray.lims.permissions.AddMaterial',
            schema_policy='dexterity',
        )

        if id in portal.portal_types:
            del portal.portal_types[id]
        portal.portal_types._setObject(id, fti)

    return "Created material types"


def setupPermissions(context):
    if context.readDataFile('immunarray.lims.txt') is None:
        return

    portal = context.getSite()

    mp = portal.materials.manage_permission
    mp(AddMaterial['Manager', 'Owner'], 1)

def setupVarious(context):
    if context.readDataFile('immunarray.lims.txt') is None:
        return

    portal = context.getSite()

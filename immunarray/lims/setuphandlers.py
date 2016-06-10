# -*- coding: utf-8 -*-
from Products.ATContentTypes.lib.constraintypes import ENABLED
from Products.CMFPlone.interfaces import ISelectableConstrainTypes
from immunarray.lims import messageFactory as _
from immunarray.lims.permissions import AddMaterial
from plone import api
from plone.app.dexterity import MessageFactory as _
from plone.dexterity.fti import DexterityFTI
from zope.interface import alsoProvides
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
        # base FTI can contain "material".
        folder_fti = portal.portal_types['Folder']
        material_fti = portal.portal_types['material']

        # import pdb
        # pdb.set_trace()
        #
        # folder_fti.manage_changeProperties(
        #     allowed_types=types)
        # view = folder.restrictedTraverse('@@select_default_page')()

    # built-in materials
    materials = [
        ('caseinsalt', _(u"Casein Salt"), """<model xmlns:lingua="http://namespaces.plone.org/supermodel/lingua"
             xmlns:users="http://namespaces.plone.org/supermodel/users"
             xmlns:security="http://namespaces.plone.org/supermodel/security"
             xmlns:marshal="http://namespaces.plone.org/supermodel/marshal"
             xmlns:form="http://namespaces.plone.org/supermodel/form"
             xmlns="http://namespaces.plone.org/supermodel/schema">
          <schema>
            <field name="randomfield" type="zope.schema.Choice">
              <description>This field is available in casein salt materials only.</description>
              <title>Casine Salt Random Field</title>
              <values>
                <element>42</element>
                <element>111</element>
                <element>256</element>
              </values>
            </field>
          </schema>
        </model>"""),
        ('ethylalcoholdenatured', _(u"Ethylalcahol Denatured"),
         """<model xmlns="http://namespaces.plone.org/supermodel/schema"><schema></schema></model>"""),
        ('glycerol', _(u"Glycerol"),
         """<model xmlns="http://namespaces.plone.org/supermodel/schema"><schema></schema></model>"""),
        ('kcl', _(u"Potassium Chloride (KCl)"),
         """<model xmlns="http://namespaces.plone.org/supermodel/schema"><schema></schema></model>"""),
        ('kcl', _(u"Potassium Chloride (KCl)"),
         """<model xmlns="http://namespaces.plone.org/supermodel/schema"><schema></schema></model>"""),
        ('kh2po4', _(u"Potassium Phosphatemonobasic (KH2PO4)"),
         """<model xmlns="http://namespaces.plone.org/supermodel/schema"><schema></schema></model>"""),
    ]

    for id, title, schema in materials:
        fti = DexterityFTI(id)
        fti.id = id

        fti.manage_changeProperties(
            factory=id,
            title=title.encode('utf8'),
            description=u"Type information for %s" % title.encode(),
            i18n_domain='immunarray.lims',
            klass='immunarray.lims.interfaces.material.IMaterial',
            model_source=schema,
            immediate_view='folder_contents',
            icon_expr='string:document_icon.png',
            # add_view_expr='string:${folder_url}/++add+' + id,
            filter_content_types=True,
            allowed_content_types=[],
            global_allow=True,
            behaviors=[
                "immunarray.lims.interfaces.material.IMaterial",
            ],
            add_permission='immunarray.lims.permissions.AddMaterial',
        )

        if id in portal.portal_types:
            del portal.portal_types[id]
        portal.portal_types._setObject(id, fti)

        constraints = ISelectableConstrainTypes(portal.materials)
        constraints.setConstrainTypesMode(ENABLED)

        import sys
        import pdb
        for attr in ('stdin', 'stdout', 'stderr'):
            setattr(sys, attr, getattr(sys, '__%s__' % attr))
        pdb.set_trace()

        constraints.setLocallyAllowedTypes(('material',))


    return "Created material types"


def setupPermissions(context):
    if context.readDataFile('immunarray.lims.txt') is None:
        return

    portal = context.getSite()

    mp = portal.materials.manage_permission
    mp(AddMaterial, ['Manager', 'Owner'], 0)


def setupVarious(context):
    if context.readDataFile('immunarray.lims.txt') is None:
        return

    portal = context.getSite()

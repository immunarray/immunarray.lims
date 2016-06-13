# -*- coding: utf-8 -*-
from Products.ATContentTypes.lib.constraintypes import ENABLED
from Products.CMFPlone.interfaces import ISelectableConstrainTypes
from immunarray.lims import messageFactory as _
from immunarray.lims.permissions import AddMaterial
from immunarray.lims.permissions import AddSolution
from plone import api
from plone.app.dexterity import MessageFactory as _
from plone.dexterity.fti import DexterityFTI
from zope.interface import alsoProvides
from zope.lifecycleevent import modified


def setupContent(context):
    if context.readDataFile('immunarray.lims.txt') is None:
        return
    portal = context.getSite()

    for x in [
        {'id': 'materials', 'type': 'Folder', 'title': 'Materials'},
        {'id': 'solutions', 'type': 'Folder', 'title': 'Solutions'}
    ]:
        if x['id'] not in portal:
            folder = api.content.create(container=portal,
                                        id=x['id'],
                                        type=x['type'],
                                        title=x['title'])
            modified(portal[x['id']])
            # Remove default allowed content types from folder
            # folder.setConstrainTypesMode(1)
            # folder.setLocallyAllowedTypes(("Collection", "File",))
            # folder.setImmediatelyAddableTypes(("Collection", "File",))
            # from Products.CMFPlone.interfaces import IConstrainTypes
            # folder = IConstrainTypes(folder)
            # folder.setLocallyAllowedTypes([])
            # folder.setImmediatelyAddableTypes([])


def setupMaterials(context):
    """Configure a set of Material types.  In normal operation, these can be
    defined direcly by adding new Dexterity types and applying the IMaterial
    behaviour to them.
    """
    if context.readDataFile('immunarray.lims.txt') is None:
        return
    portal = context.getSite()

    # built-in materials
    materials = [
        ("caseinsalt", _(u"Casein Salt"),
         """<model xmlns="http://namespaces.plone.org/supermodel/schema"><schema></schema></model>"""),
        ("ethylalcohol", _(u"Ethyl Alcahol Denatured"),
         """<model xmlns="http://namespaces.plone.org/supermodel/schema"><schema></schema></model>"""),
        ("glycerol", _(u"Glycerol"),
         """<model xmlns="http://namespaces.plone.org/supermodel/schema"><schema></schema></model>"""),
        ("nacl", _(u"Sodium Chloride (NaCl)"),
         """<model xmlns="http://namespaces.plone.org/supermodel/schema"><schema></schema></model>"""),
        ("kcl", _(u"Potassium Chloride (KCl)"),
         """<model xmlns="http://namespaces.plone.org/supermodel/schema"><schema></schema></model>"""),
        ("kh2po4", _(u"Potassium Phosphatemonobasic (KH2PO4)"),
         """<model xmlns="http://namespaces.plone.org/supermodel/schema"><schema></schema></model>"""),
        ("na2hpo4", _(u"Sodium Phosphatedibasic (Na2HPO4)"),
         """<model xmlns="http://namespaces.plone.org/supermodel/schema"><schema></schema></model>"""),
        ("naoh", _(u"Sodium Hydroxide 2.5N (NaOH)"),
         """<model xmlns="http://namespaces.plone.org/supermodel/schema"><schema></schema></model>"""),
        ("tween20", _(u"Tween 20"),
         """<model xmlns="http://namespaces.plone.org/supermodel/schema"><schema></schema></model>"""),
        ("hcl37", _(u"Hydrochloricacid 37%"),
         """<model xmlns="http://namespaces.plone.org/supermodel/schema"><schema></schema></model>"""),
        ("iggcy3", _(u"IgG-Cy3"),
         """<model xmlns="http://namespaces.plone.org/supermodel/schema"><schema></schema></model>"""),
        ("igmaf647", _(u"IgM-AF647"),
         """<model xmlns="http://namespaces.plone.org/supermodel/schema"><schema></schema></model>"""),
    ]

    for tid, title, schema in materials:
        fti = DexterityFTI(tid)
        fti.manage_changeProperties(
            factory=tid,
            title=title.encode('utf8'),
            description=u"Material %s" % title.encode(),
            i18n_domain='immunarray.lims',
            klass='immunarray.lims.interfaces.material.IMaterial',
            model_source=schema,
            immediate_view='folder_contents',
            icon_expr='string:document_icon.png',
            filter_content_types=True,
            allowed_content_types=[],
            global_allow=True,
            behaviors=[
                "immunarray.lims.interfaces.material.IMaterial",
            ],
            add_permission='immunarray.lims.permissions.AddMaterial',
        )
        if tid in portal.portal_types:
            del portal.portal_types[tid]
        portal.portal_types._setObject(tid, fti)

    return "Created built-in material types"


def setupSolutions(context):
    """Configure a set of Solution types.  In normal operation, these can be
    defined direcly by adding new Dexterity types and applying the ISolution
    behaviour to them.
    """
    if context.readDataFile('immunarray.lims.txt') is None:
        return
    portal = context.getSite()

    solutions = [
        # ('caseinsalt', _(u"Casein Salt"),
        # """<model xmlns:lingua="http://namespaces.plone.org/supermodel/lingua"
        #      xmlns:users="http://namespaces.plone.org/supermodel/users"
        #      xmlns:security="http://namespaces.plone.org/supermodel/security"
        #      xmlns:marshal="http://namespaces.plone.org/supermodel/marshal"
        #      xmlns:form="http://namespaces.plone.org/supermodel/form"
        #      xmlns="http://namespaces.plone.org/supermodel/schema">
        #   <schema>
        #     <field name="randomfield" type="zope.schema.Choice">
        #       <description>This field is available in casein salt materials only.</description>
        #       <title>Casine Salt Random Field</title>
        #       <values>
        #         <element>42</element>
        #         <element>111</element>
        #         <element>256</element>
        #       </values>
        #     </field>
        #   </schema>
        # </model>"""),
        ("1xpbs", _(u"PBS (1X)"),
         """<model xmlns="http://namespaces.plone.org/supermodel/schema"><schema></schema></model>"""),
        ("10xpbs", _(u"PBS (10X)"),
         """<model xmlns="http://namespaces.plone.org/supermodel/schema"><schema></schema></model>"""),
        ("1percentcasein", _(u"1% Casein in PBS"),
         """<model xmlns="http://namespaces.plone.org/supermodel/schema"><schema></schema></model>"""),
        ("tween22_4percentinpbs", _(u"22.4% Tween in PBS"),
         """<model xmlns="http://namespaces.plone.org/supermodel/schema"><schema></schema></model>"""),
        ("70percentethyanol", _(u"70% Ethyanol (Cleaning Solution)"),
         """<model xmlns="http://namespaces.plone.org/supermodel/schema"><schema></schema></model>"""),
        ("50percentglycerol", _(u"50% Glycerol"),
         """<model xmlns="http://namespaces.plone.org/supermodel/schema"><schema></schema></model>"""),
        ("10percenthcl", _(u"10% HCl"),
         """<model xmlns="http://namespaces.plone.org/supermodel/schema"><schema></schema></model>"""),
        ("3Mkcl", _(u"3M KCl"),
         """<model xmlns="http://namespaces.plone.org/supermodel/schema"><schema></schema></model>"""),
        ("1mgpermligm_af647", _(u"1 mg/mL IgM-AF647"),
         """<model xmlns="http://namespaces.plone.org/supermodel/schema"><schema></schema></model>"""),
        ("1mgpermligg_cy3", _(u"1 mg/mL IgG-Cy3"),
         """<model xmlns="http://namespaces.plone.org/supermodel/schema"><schema></schema></model>""")
    ]
    for tid, title, schema in solutions:
        fti = DexterityFTI(tid)
        fti.manage_changeProperties(
            factory=tid,
            title=title.encode('utf8'),
            description=u"Solution: %s" % title.encode(),
            i18n_domain='immunarray.lims',
            klass='immunarray.lims.interfaces.solution.ISolution',
            model_source=schema,
            immediate_view='folder_contents',
            icon_expr='string:document_icon.png',
            filter_content_types=True,
            allowed_content_types=[],
            global_allow=True,
            behaviors=[
                "immunarray.lims.interfaces.solution.ISolution",
            ],
            add_permission='immunarray.lims.permissions.AddSolution',
        )
        if tid in portal.portal_types:
            del portal.portal_types[tid]
        portal.portal_types._setObject(tid, fti)

    return "Created built-in solution types"


def setupPermissions(context):
    if context.readDataFile('immunarray.lims.txt') is None:
        return
    portal = context.getSite()

    mp = portal.materials.manage_permission
    mp(AddMaterial, ['Manager', 'Owner'], 0)

    mp = portal.solutions.manage_permission
    mp(AddSolution, ['Manager', 'Owner'], 0)


def setupVarious(context):
    if context.readDataFile('immunarray.lims.txt') is None:
        return
    portal = context.getSite()

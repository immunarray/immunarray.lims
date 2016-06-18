# -*- coding: utf-8 -*-
from pkg_resources import resource_filename
from plone import api
from plone.dexterity.fti import DexterityFTI
from zope.component.hooks import getSite

from immunarray.lims.permissions import AddMaterial, AddSolution

def get_schema_filename(folder, name):
    return resource_filename('immunarray.lims', '%s/%s.xml' % (folder, name))

def LIMSCreated(event):
    """LIMS root object has been created
    Here we will add the ImmunArray specific objects and configuration.
    """
    lims = event.lims
    portal = getSite()

    configuration = lims.configuration
    m = api.content.create(configuration, 'Folder', 'materials', 'Materials')
    mp = m.manage_permission
    mp(AddMaterial, ['Manager', 'LabManager', 'Owner'], 0)

    s = api.content.create(configuration, 'Folder', 'solutions', 'Solutions')
    mp = s.manage_permission
    mp(AddSolution, ['Manager', 'LabManager', 'LabClerk', 'Owner'], 0)

    # built-in material types and schemas
    # -----------------------------------
    materials = [
        ("caseinsalt", u"Casein Salt"),
        ("ethylalcohol", u"Ethyl Alcahol Denatured"),
        ("glycerol", u"Glycerol"),
        ("nacl", u"Sodium Chloride (NaCl)"),
        ("kcl", u"Potassium Chloride (KCl)"),
        ("kh2po4", u"Potassium Phosphatemonobasic (KH2PO4)"),
        ("na2hpo4", u"Sodium Phosphatedibasic (Na2HPO4)"),
        ("naoh", u"Sodium Hydroxide 2.5N (NaOH)"),
        ("tween20", u"Tween 20"),
        ("hcl37", u"Hydrochloricacid 37%"),
        ("iggcy3", u"IgG-Cy3"),
        ("igmaf647", u"IgM-AF647"),
    ]

    for tid, title in materials:
        fti = DexterityFTI(tid)
        fti.manage_changeProperties(
            factory=tid,
            title=title.encode('utf8'),
            description=u"Material: {0}".format(title.encode()),
            i18n_domain='immunarray.lims',
            klass='immunarray.lims.interfaces.material.IMaterial',
            model_file=get_schema_filename('materials', tid),
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

    solutions = [
        ("1xpbs", u"PBS (1X)"),
        ("10xpbs", u"PBS (10X)"),
        ("1percentcasein", u"1% Casein in PBS"),
        ("70percentethanol", u"70% Ethanol (Cleaning Solution)"),
        ("tween22_4percentinpbs", u"22.4% Tween in PBS"),
        ("50percentglycerol", u"50% Glycerol"),
        ("10percenthcl", u"10% HCl"),
        ("3mkcl", u"3M KCl"),
        ("1mgpermligm_af647", u"1 mg/mL IgM-AF647"),
        ("1mgpermligg_cy3", u"1 mg/mL IgG-Cy3"),
    ]

    for tid, title in solutions:
        fti = DexterityFTI(tid)
        fti.manage_changeProperties(
            factory=tid,
            title=title.encode('utf8'),
            description=u"Solution: {0}".format(title.encode()),
            i18n_domain='immunarray.lims',
            klass='immunarray.lims.interfaces.solution.ISolution',
            model_file=get_schema_filename('solutions', tid),
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

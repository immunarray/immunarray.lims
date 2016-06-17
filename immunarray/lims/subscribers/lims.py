# -*- coding: utf-8 -*-
from plone import api
from plone.dexterity.fti import DexterityFTI
from zope.component.hooks import getSite

from immunarray.lims.permissions import AddMaterial, AddSolution


def LIMSCreated(lims, event):
    """LIMS root object has been created
    Here we will add the ImmunArray specific objects and configuration.
    """
    portal = getSite()

    import sys
    import pdb
    for attr in ('stdin', 'stdout', 'stderr'):
        setattr(sys, attr, getattr(sys, '__%s__' % attr))
    pdb.set_trace()
    

    configuration = lims.configuration
    m = api.content.create(configuration, 'Folder', 'materials', 'Materials')
    m.manage_permission(AddMaterial,
                        ['Manager', 'LabManager', 'Owner'], 0)

    s = api.content.create(configuration, 'Folder', 'solutions', 'Solutions')
    s.manage_permission(AddSolution,
                        ['Manager', 'LabManager', 'LabClerk', 'Owner'], 0)

    # built-in material types and schemas
    # -----------------------------------
    materials = [
        (u"caseinsalt", u"Casein Salt",
         """<model xmlns="http://namespaces.plone.org/supermodel/schema">
             <schema>
             </schema></model>"""),
        (u"ethylalcohol", u"Ethyl Alcahol Denatured",
         """<model xmlns="http://namespaces.plone.org/supermodel/schema">
             <schema>
             </schema></model>"""),
        (u"glycerol", u"Glycerol",
         """<model xmlns="http://namespaces.plone.org/supermodel/schema">
             <schema>
             </schema></model>"""),
        (u"nacl", u"Sodium Chloride (NaCl)",
         """<model xmlns="http://namespaces.plone.org/supermodel/schema">
             <schema>
             </schema></model>"""),
        (u"kcl", u"Potassium Chloride (KCl)",
         """<model xmlns="http://namespaces.plone.org/supermodel/schema">
             <schema>
             </schema></model>"""),
        (u"kh2po4", u"Potassium Phosphatemonobasic (KH2PO4)",
         """<model xmlns="http://namespaces.plone.org/supermodel/schema">
             <schema>
             </schema></model>"""),
        (u"na2hpo4", u"Sodium Phosphatedibasic (Na2HPO4)",
         """<model xmlns="http://namespaces.plone.org/supermodel/schema">
             <schema>
             </schema></model>"""),
        (u"naoh", u"Sodium Hydroxide 2.5N (NaOH)",
         """<model xmlns="http://namespaces.plone.org/supermodel/schema">
             <schema>
             </schema></model>"""),
        (u"tween20", u"Tween 20",
         """<model xmlns="http://namespaces.plone.org/supermodel/schema">
             <schema>
             </schema></model>"""),
        (u"hcl37", u"Hydrochloricacid 37%",
         """<model xmlns="http://namespaces.plone.org/supermodel/schema">
             <schema>
             </schema></model>"""),
        (u"iggcy3", u"IgG-Cy3",
         """<model xmlns="http://namespaces.plone.org/supermodel/schema">
             <schema>
             </schema></model>"""),
        (u"igmaf647", u"IgM-AF647",
         """<model xmlns="http://namespaces.plone.org/supermodel/schema">
             <schema>
             </schema></model>"""),
    ]

    for tid, title, schema in materials:
        fti = DexterityFTI(tid)
        fti.manage_changeProperties(
            factory=tid,
            title=title.encode('utf8'),
            description=u"Material: {0}".format(title.encode()),
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

    solutions = [
        (u"1xpbs", u"PBS (1X)", """
<model xmlns:form="http://namespaces.plone.org/supermodel/form"
xmlns:i18n="http://xml.zope.org/namespaces/i18n"
xmlns:lingua="http://namespaces.plone.org/supermodel/lingua"
xmlns:marshal="http://namespaces.plone.org/supermodel/marshal"
xmlns:security="http://namespaces.plone.org/supermodel/security"
xmlns:users="http://namespaces.plone.org/supermodel/users"
xmlns="http://namespaces.plone.org/supermodel/schema">
  <schema>
    <field name="batch_of_10_x_pbs_used"
    type="z3c.relationfield.schema.RelationChoice">
      <title>Batch of 10x PBS Used</title>
      <description/>
      <required>False</required>
      <portal_type>
        <element>plate96well</element>
      </portal_type>
    </field>
    <field name="volumeof10xpbsadded" type="zope.schema.Float">
      <title>Volume of 10x PBS Added</title>
      <description>(in liters)</description>
      <required>False</required>
    </field>
    <field name="volume_of_water_added" type="zope.schema.Float">
      <title>Volume of Water Added to 10x PBS</title>
      <description>(in liters)</description>
      <required>False</required>
    </field>
    <field name="pbs_1x_verify_ph_meter" type="zope.schema.TextLine">
      <title>Verify pH</title>
      <description></description>
      <required>False</required>
    </field>
    <field name="observed_ph_of_1_x_pbs" type="zope.schema.TextLine">
      <title>Observed pH of 1 x PBS</title>
      <description>(xxx)</description>
      <required>False</required>
    </field>
  </schema>
</model>"""),
        (u"10xpbs", u"PBS (10X)", """
<model xmlns:form="http://namespaces.plone.org/supermodel/form"
xmlns:i18n="http://xml.zope.org/namespaces/i18n"
xmlns:lingua="http://namespaces.plone.org/supermodel/lingua"
xmlns:marshal="http://namespaces.plone.org/supermodel/marshal"
xmlns:security="http://namespaces.plone.org/supermodel/security"
xmlns:users="http://namespaces.plone.org/supermodel/users"
xmlns="http://namespaces.plone.org/supermodel/schema">
  <schema>
    <field name="volume_of_water_added_to_10xpbs" type="zope.schema.Float">
      <title>Volume of water added to 10xPBS</title>
      <description>(in liters)</description>
      <required>False</required>
    </field>
    <field name="sodium_chloride_lot"
           type="z3c.relationfield.schema.RelationChoice">
      <title>Sodium Chloride Lot</title>
      <description>Lot of Sodium Chloride Added</description>
      <required>False</required>
      <portal_type>
        <element>material</element>
      </portal_type>
    </field>
    <field name="mass_of_sodium_chloride" type="zope.schema.Float">
      <title>Mass of Sodium Chloride Added</title>
      <description>(in grams)</description>
      <required>False</required>
    </field>
    <field name="potassium_chloride_lot"
           type="z3c.relationfield.schema.RelationChoice">
      <title>Potassium Chloride Lot</title>
      <description>Lot of Potassium Chloride Added</description>
      <required>False</required>
      <portal_type>
        <element>material</element>
      </portal_type>
    </field>
    <field name="mass_of_potassium_chloride" type="zope.schema.Float">
      <title>Mass of Potassium Chloride Added</title>
      <description>(in grams)</description>
      <required>False</required>
    </field>
    <field name="sodiumphosphate_dibasic_lot"
           type="z3c.relationfield.schema.RelationChoice">
      <title>Sodium Phosphate Dibasic Lot</title>
      <description>Lot of Sodium Phosphate Dibasic Added</description>
      <required>False</required>
      <portal_type>
        <element>material</element>
      </portal_type>
    </field>
    <field name="mass_of_sodiumphosphate_dibasic" type="zope.schema.Float">
      <title>Mass of Sodium Phosphate Dibasic Added</title>
      <description>(in grams)</description>
      <required>False</required>
    </field>
    <field name="potassiumphosphate_monobasic_lot"
           type="z3c.relationfield.schema.RelationChoice">
      <title>Potassium Phosphate Monobasic Lot</title>
      <description>Lot of Potassium Phosphate Monobasic Added</description>
      <required>False</required>
      <portal_type>
        <element>material</element>
      </portal_type>
    </field>
    <field name="mass_of_potassiumphosphate_monobasic" type="zope.schema.Float">
      <title>Mass of Potassium Phosphate Monobasic Added</title>
      <description>(in grams)</description>
      <required>False</required>
    </field>
    <field name="verify_ph_meter" type="zope.schema.TextLine">
      <title>Verify pH</title>
      <description>Measured pH of PBS (10X)</description>
      <required>False</required>
    </field>
    <field name="observed_ph_of_1_x_pbs" type="zope.schema.TextLine">
      <title>Observed pH of 1 x PBS</title>
      <description>Observed pH Post HCl or NaOH Addition</description>
      <required>False</required>
    </field>
  </schema>
</model>"""),
        (u"1percentcasein", u"1% Casein in PBS", """
<model xmlns:form="http://namespaces.plone.org/supermodel/form"
xmlns:i18n="http://xml.zope.org/namespaces/i18n"
xmlns:lingua="http://namespaces.plone.org/supermodel/lingua"
xmlns:marshal="http://namespaces.plone.org/supermodel/marshal"
xmlns:security="http://namespaces.plone.org/supermodel/security"
xmlns:users="http://namespaces.plone.org/supermodel/users"
xmlns="http://namespaces.plone.org/supermodel/schema">
  <schema>
    <field name="lot_of_casein_salt"
    type="z3c.relationfield.schema.RelationChoice">
      <title>Lot of Casein Salt Used</title>
      <description></description>
      <required>False</required>
      <portal_type>
        <element>material</element>
      </portal_type>
    </field>
    <field name="lot_of_1xpbs" type="z3c.relationfield.schema.RelationChoice">
      <title>Lot of PBS (1X) Used</title>
      <description></description>
      <required>False</required>
      <portal_type>
        <element>material</element>
      </portal_type>
    </field>
    <field name="mass_of_casein_salt" type="zope.schema.Float">
      <title>Mass of Casein Salt Added to PBS</title>
      <description>(in grams)</description>
      <required>False</required>
    </field>
    <field name="volume_of_1xpbs" type="zope.schema.Float">
      <title>Volume of 1 x PBS Added</title>
      <description>(in liters)</description>
      <required>False</required>
    </field>
  </schema>
</model>"""),
        (u"70percentethanol", u"70% Ethanol (Cleaning Solution)", """
<model xmlns:form="http://namespaces.plone.org/supermodel/form"
xmlns:i18n="http://xml.zope.org/namespaces/i18n"
xmlns:lingua="http://namespaces.plone.org/supermodel/lingua"
xmlns:marshal="http://namespaces.plone.org/supermodel/marshal"
xmlns:security="http://namespaces.plone.org/supermodel/security"
xmlns:users="http://namespaces.plone.org/supermodel/users"
xmlns="http://namespaces.plone.org/supermodel/schema">
  <schema>
    <field name="volume_of_ethanol" type="zope.schema.Float">
      <title>Volume of ethanol added</title>
      <description>(in liters)</description>
      <required>False</required>
    </field>
  </schema>
</model>"""),
        (u"tween22_4percentinpbs", u"22.4% Tween in PBS",
         """<model xmlns="http://namespaces.plone.org/supermodel/schema>
             <schema>
             </schema></model>"""),
        (u"50percentglycerol", u"50% Glycerol",
         """<model xmlns="http://namespaces.plone.org/supermodel/schema>
             <schema>
             </schema></model>"""),
        (u"10percenthcl", u"10% HCl",
         """<model xmlns="http://namespaces.plone.org/supermodel/schema>
             <schema>
             </schema></model>"""),
        (u"3mkcl", u"3M KCl",
         """<model xmlns="http://namespaces.plone.org/supermodel/schema>
             <schema>
             </schema></model>"""),
        (u"1mgpermligm_af647", u"1 mg/mL IgM-AF647",
         """<model xmlns="http://namespaces.plone.org/supermodel/schema>
             <schema>
             </schema></model>"""),
        (u"1mgpermligg_cy3", u"1 mg/mL IgG-Cy3",
         """<model xmlns="http://namespaces.plone.org/supermodel/schema>
            <schema>
            </schema></model>""")
    ]
    for tid, title, schema in solutions:
        fti = DexterityFTI(tid)
        fti.manage_changeProperties(
            factory=tid,
            title=title.encode('utf8'),
            description=u"Solution: {0}".format(title.encode()),
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

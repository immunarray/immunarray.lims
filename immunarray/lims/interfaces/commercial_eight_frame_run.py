from datetime import date
from immunarray.lims.interfaces.veracisrunbase import IVeracisRunBase
from immunarray.lims import messageFactory as _
from plone.app.textfield import RichText
from plone.supermodel import model
from zope import schema
from plone.autoform.interfaces import IFormFieldProvider
from immunarray.lims.vocabularies.ichip import *
from immunarray.lims.vocabularies import ichip
from immunarray.lims.vocabularies.ichipassay import IChipAssayListVocabulary
from immunarray.lims.vocabularies import ichipassay
from immunarray.lims.vocabularies.provider import ProvidersVocabulary
from z3c.relationfield import RelationChoice
from plone.directives import form
from plone import api
from plone.i18n.normalizer.interfaces import IIDNormalizer
from zope.component import queryUtility
from zope.interface import implements, Interface, implementer
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.interfaces import IContextSourceBinder
from Products.CMFCore.interfaces import IContentish
from Products.CMFCore.utils import getToolByName
from zope.interface import alsoProvides
from plone.app.z3cform.widget import *
from plone.autoform import directives
from z3c.form import form, button

class ICommercailEightFrameRun(IVeracisRunBase):
    """Eight Frame Test Run
    """
    aliquot_to_well = schema.Dict(
        key_type=schema.TextLine(title=u"Aliquot ID", required=False),
        value_type=schema.Choice(source=ICommercailThreeFrameChipWellsVocabulary, required=False)
    )

    # Solutions
    ten_x_pbs = schema.TextLine(
        title=_(u"10X PBS Lot Used"),
        description=_(u"10X PBS Lot Used"),
        required=False,
    )

    one_x_pbs = schema.TextLine(
        title=_(u"1X PBS Lot Used"),
        description=_(u"1X PBS Lot Used"),
        required=False,
    )

    one_x_pbs_casein = schema.TextLine(
        title=_(u"1X PBS 1% Casein Lot Used"),
        description=_(u"1X PBS 1% Casein Lot Used"),
        required=False,
    )

    one_x_pbs_22_tween20 = schema.TextLine(
        title=_(u"1X PBS - 22% Tween 20 Lot Used"),
        description=_(u"1X PBS - 22% Tween 20 Lot Used"),
        required=False,
    )

    ethanol_70_percent = schema.TextLine(
        title=_(u"70% Ethanol"),
        description=_(u"70% Ethanol"),
        required=False,
    )

    antibodies_used = schema.Dict(
        key_type=schema.TextLine(title=u"Anitbody/Antigen Used",required=True),
        value_type=schema.TextLine(title=u"Lot of Anitbody/Antigen Used",required=True)
    )

    # iChip Humidity

    ichip_humidity = schema.Dict(
        key_type=schema.TextLine(title=u"iChip Print Lot",required=True),
        value_type=schema.TextLine(title=u"Humidity",required=True)
    )

    # Serum Addition
    serum_time_start = schema.Datetime(
        title=_(u"Start Time of Serum Addition"),
        description=_(u"Start Time of Serum Addition"),
        required=False,
    )
    serum_humidity_start = schema.Float(
        title=_(u"Humidity at Serum Addition Start"),
        description=_(u"Humidity at Serum Addition Start"),
        required=False,
    )
    serum_room_temperature_start = schema.Float(
        title=_(u"Room Temperature at Serum Addition Start"),
        description=_(u"Room Temperature at Serum Addition Start"),
        required=False,
    )
    serum_time_end = schema.Datetime(
        title=_(u"End Time of Serum Addition"),
        description=_(u"End Time of Serum Addition"),
        required=False,
    )
    serum_humidity_end = schema.Float(
        title=_(u"Humidity at Serum Addition End"),
        description=_(u"Humidity at Serum Addition End"),
        required=False,
    )
    serum_room_temperature_end = schema.Float(
        title=_(u"Room Temperature at Serum Addition End"),
        description=_(u"Room Temperature at Serum Addition End"),
        required=False,
    )
    # Choice of labtech/labmanager
    serum_witness_name = schema.TextLine(
        title=_(u"Witness for Serum Addition"),
        description=_(u"Witness for Serum Addition"),
        required=False,
    )
    serum_witness_date = schema.Date(
        title=_(u"Aliquot Consume Date"),
        description=_(u"Aliquot Consume Date"),
        required=False,
    )

    # Antibody Prep

    # Antibody Addition
    antibody_time_start = schema.Datetime(
        title=_(u"Start Time of Antibody Addition"),
        description=_(u"Start Time of Antibody Addition"),
        required=False,
    )
    antibody_humidity_start = schema.Float(
        title=_(u"Humidity at Antibody Addition Start"),
        description=_(u"Humidity at Antibody Addition Start"),
        required=False,
    )
    antibody_room_temperature_start = schema.Float(
        title=_(u"Room Temperature at Antibody Addition Start"),
        description=_(u"Room Temperature at Antibody Addition Start"),
        required=False,
    )
    antibody_time_end = schema.Datetime(
        title=_(u"End Time of Antibody Addition"),
        description=_(u"End Time of Antibody Addition"),
        required=False,
    )
    antibody_humidity_end = schema.Float(
        title=_(u"Humidity at Antibody Addition End"),
        description =_(u"Humidity at Antibody Addition End"),
        required=False,
    )
    antibody_room_temperature_end = schema.Float(
        title=_(u"Room Temperature at Antibody Addition End"),
        description=_(u"Room Temperature at Antibody Addition End"),
        required=False,
    )
    # Choice of labtech/labmanager
    antibody_witness_name = schema.TextLine(
        title=_(u"Witness for Antibody Addition"),
        description=_(u"Witness for Antibody Addition"),
        required=False,
    )
    antibody_witness_date = schema.Date(
        title=_(u"Aliquot Consume Date"),
        description=_(u"Aliquot Consume Date"),
        required=False,
    )


alsoProvides(IThreeFrameRun, IFormFieldProvider)

"""
from base run!
veracis_run_number = schema.Int(
        title=_(u"Veracis Run Number"),
        description=_(u"Veracis Run Number"),
        required=True,
    )
    veracis_run_purpose = schema.TextLine(
        title=_(u"Veracis Test Run Purpose"),
        description=_(u"Veracis Test Run Purpose"),
    )
    veracis_run_serial_number = schema.Int(
        title=_(u"Veracis Run Serial Number"),
        description=_(u"Veracis Run Serial Number"),
    )
    veracis_run_operator = schema.TextLine(
        title=_(u"Veracis Run Operator"),
        description=_(u"Veracis Run Operator"),
        required=True,
    )
    veracis_test_run_date = schema.Date(
        title=_(u"Veracis Test Run Date"),
        description=_(u"Veracis Test Run Date (MM/DD/YYYY)"),
        default=date.today(),
    )
    veracis_test_scan_date = schema.Date(
        title=_(u"Veracis Test Scan Date"),
        description=_(u"Veracis Test Scan Date (MM/DD/YYYYY)"),
        default=date.today(),
    )
    pdf_veracis_run = NamedBlobImage(
        title=_(u"PDF Upload of Test Form"),
        description=_(u"PDF Upload of Test Form"),
        required=False,
    )
"""

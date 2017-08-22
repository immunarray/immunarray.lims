# -*- coding: utf-8 -*-
from datetime import date
from immunarray.lims.interfaces.veracisrunbase import IVeracisRunBase
from immunarray.lims import messageFactory as _
from plone.app.textfield import RichText
from plone.supermodel import model
from zope import schema

class INoFrameRun(IVeracisRunBase):
    # Well position to aliquot id tested
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

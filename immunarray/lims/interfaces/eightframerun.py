# -*- coding: utf-8 -*-
import datetime

from immunarray.lims import messageFactory as _
from immunarray.lims.interfaces.veracisrunbase import IVeracisRunBase
from zope import schema
from zope.interface import Attribute


def currentTime():
    return datetime.datetime.now()


def currentDate():
    return datetime.datetime.now().date()


class IEightFrameRun(IVeracisRunBase):

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

    # Choice of lab tech/lab manager
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
        description=_(u"Humidity at Antibody Addition End"),
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

    assay_name = Attribute("""Assay Name
    Assay name is stored here so that the edit form has an exact copy.
    """)

    plates = Attribute("""Plates
    A map of aliquots/ichips/wells per plate is stored here as a list
    of dictionaries. The format matches what is excpected by the form,
    which is the same as the data returned when creating a new test run.
    """)

    ichip_humidity = Attribute("""iChip Humidity
    Humidity is logged before and after each ichip is prepared.
    """)

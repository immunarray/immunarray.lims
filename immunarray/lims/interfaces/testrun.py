# -*- coding: utf-8 -*-
import datetime
from zope import schema

from immunarray.lims import messageFactory as _
from immunarray.lims.interfaces.veracisrunbase import IVeracisRunBase
from zope.interface import Attribute


def currentTime():
    return datetime.datetime.now()


def currentDate():
    return datetime.datetime.now().date()


class ITestRun(IVeracisRunBase):
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

    assay_uid = Attribute("""Assay UID
    Link directly back to the iChipAssay so that the edit form has a copy
    when required.  Also used to link QC aliquots back to the HQC and LQC
    of the selected Assay.
    """)

    assay_name = Attribute("""Assay Name
    For convenience, I'll store the assay_name too, but it should not be used
    for lookup.
    """)

    plates = Attribute("""Plates
    A map of aliquots/ichips/wells per plate is stored here as a list
    of dictionaries. The format matches what is excpected by the form,
    which is the same as the data returned when creating a new test run.
    
    The format of each plate looks like this:
      {'chip-1_well-1': UID,
       'chip-1_well-X': UID,
       'chip-2_well-1': UID,
       'chip-2_well-X': UID,
       'chip-3_well-1': UID,
       'chip-3_well-X': UID,
       'chip-4_well-1': UID,
       'chip-4_well-X': UID,
       'chip-id-1': UID,
       'chip-id-2': UID,
       'chip-id-3': UID,
       'chip-id-4': UID,
       'comments-ichip-1': '',
       'comments-ichip-2': '',
       'comments-ichip-3': '',
       'comments-ichip-4': '',
       'scan-slot-1': '',
       'scan-slot-2': '',
       'scan-slot-3': '',
       'scan-slot-4': '',
       'comments': ''
       }
    """)

    solutions = Attribute("""Solution batches in use
    Details of all solution batches selected for use in this run, stored
    as a list of lists like this:
    
    [list of solution batch ids]
    
    """)

    ichip_humidity = Attribute("""iChip Humidity
    Humidity is logged before and after each ichip is prepared.
    """)

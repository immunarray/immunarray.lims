# -*- coding: utf-8 -*-
import datetime

from immunarray.lims import messageFactory as _
from immunarray.lims.interfaces.veracisrunbase import IVeracisRunBase
from plone.autoform.interfaces import IFormFieldProvider
from zope import schema
from zope.interface import alsoProvides, Attribute


def currentTime():
    return datetime.datetime.now()


def currentDate():
    return datetime.datetime.now().date()


class IEightFrameRun(IVeracisRunBase):

    plates = Attribute(""" """)

    # XXX ichipassay <->
    # solutions = Attribute("""Materials and/or solutions used.
    # [{'uid': UID,
    #   'lot': lot_number,
    #   'exp.date': date}]""")

    # iChip Humidity

    ichip_humidity = Attribute(""" ichiplot and humidity""")

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


alsoProvides(IFormFieldProvider)

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

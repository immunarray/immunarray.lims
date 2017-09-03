# -*- coding: utf-8 -*-
from datetime import date

from immunarray.lims import messageFactory as _
from immunarray.lims.interfaces import BaseModel
from plone.namedfile.field import NamedBlobImage
from zope import schema


class IVeracisRunBase(BaseModel):
    """Object that will be the base of all veracis runs
    """
    veracis_run_number = schema.Int(
        title=_(u"Veracis Run Number"),
        description=_(u"Veracis Run Number"),
        required=True,
    )

    # deprecated?
    # veracis_run_purpose = schema.TextLine(
    #     title=_(u"Veracis Test Run Purpose"),
    #     description=_(u"Veracis Test Run Purpose"),
    # )

    veracis_run_planner = schema.TextLine(
        title=_(u"Veracis Run Planner"),
        description=_(u"Veracis Run Operator"),
        required=True,
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

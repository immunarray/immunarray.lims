# -*- coding: utf-8 -*-
import datetime

from immunarray.lims import messageFactory as _
from immunarray.lims.content.abstractsample import assignPlateID
from immunarray.lims.interfaces.sample import ISample
from immunarray.lims.interfaces.solution import *
from zope import schema
from zope.interface import alsoProvides


def currentTime():
    return datetime.datetime.now()


def currentDate():
    return datetime.datetime.now().date()


class IAliquotPlate(ISample):
    """Aliquot Plate!
    """
    id = schema.TextLine(
        title=_(u"Aliquot Plate ID"),
        description=_(u"Aliquot Plate ID"),
        defaultFactory=assignPlateID(),
        required=True,
    )
    #date info
    
    date_added = schema.Date(
        title=_(u"Date Aliquot Plate was added to LIMS"),
        description=_(u"Date Aliquot Platee was added to LIMS"),
        defaultFactory=currentDate,
        required=True,
    )

    added_by = schema.Choice(
        title=_(u"Operator that Added Aliquot Plate to LIMS"),
        description=_(u"Operator that Added Aliquot Plate to LIMS"),
        vocabulary=u"plone.principalsource.Users",
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
    
    plates_96_well = Attribute("""Plates
        A map of aliquots to wells on a plate and is stored here as a list
        of dictionaries. The format matches what is excpected by the form,
        which is the same as the data returned when creating a new test run.
        A-H, and 12 wells
        The format of each 96 well plate looks like this:
          {'A01': UID,
           'A02': UID,
           'A03': UID,
           'A04': UID,
           'A05': UID,
           'A06': UID,
           'A07': UID,
           'A08': UID,
           'A09': UID,
           'A10': UID,
           'A11': UID,
           'A12': UID,
           'B01': UID,
           'B02': UID,
           'B03': UID,
           'B04': UID,
           'B05': UID,
           'B06': UID,
           'B07': UID,
           'B08': UID,
           'B09': UID,
           'B10': UID,
           'B11': UID,
           'B12': UID,
           'C01': UID,
           'C02': UID,
           'C03': UID,
           'C04': UID,
           'C05': UID,
           'C06': UID,
           'C07': UID,
           'C08': UID,
           'C09': UID,
           'C10': UID,
           'C11': UID,
           'C12': UID,
           'D01': UID,
           'D02': UID,
           'D03': UID,
           'D04': UID,
           'D05': UID,
           'D06': UID,
           'D07': UID,
           'D08': UID,
           'D09': UID,
           'D10': UID,
           'D11': UID,
           'D12': UID,
           'E01': UID,
           'E02': UID,
           'E03': UID,
           'E04': UID,
           'E05': UID,
           'E06': UID,
           'E07': UID,
           'E08': UID,
           'E09': UID,
           'E10': UID,
           'E11': UID,
           'E12': UID,
           'F01': UID,
           'F02': UID,
           'F03': UID,
           'F04': UID,
           'F05': UID,
           'F06': UID,
           'F07': UID,
           'F08': UID,
           'F09': UID,
           'F10': UID,
           'F11': UID,
           'F12': UID,
           'G01': UID,
           'G02': UID,
           'G03': UID,
           'G04': UID,
           'G05': UID,
           'G06': UID,
           'G07': UID,
           'G08': UID,
           'G09': UID,
           'G10': UID,
           'G11': UID,
           'G12': UID,
           'H01': UID,
           'H02': UID,
           'H03': UID,
           'H04': UID,
           'H05': UID,
           'H06': UID,
           'H07': UID,
           'H08': UID,
           'H09': UID,
           'H10': UID,
           'H11': UID,
           'H12': UID,
           }
        """)
    # source_id_one = schema.TextLine(
    #     title=_(u"Primary QC Source Sample ID"),
    #     description=_(u"Primary QC Source Sample ID"),
    #     required=True,
    # )
    # 
    # source_id_two = schema.TextLine(
    #     title=_(u"Secondary QC Source Sample ID"),
    #     description=_(u"Secondary QC Source Sample ID"),
    #     required=False,
    # )
    # 
    # source_id_three = schema.TextLine(
    #     title=_(u"Tertiary QC Source Sample ID"),
    #     description=_(u"Tertiary QC Source Sample ID"),
    #     required=False,
    # )


    description = schema.TextLine(
        title=_(u"Description of Aliquot Plate"),
        description=_(u"Description of Aliquot Plate"),
        required=False,
    )

    comment = schema.Text(
        title=_(u"Any Notes or Comments About the QC Sample"),
        description=_(u"Any Notes or Comments About the QC Sample"),
        required=False,
    )


alsoProvides(IAliquotPlate, IFormFieldProvider)

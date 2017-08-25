# -*- coding: utf-8 -*-
import datetime

from Products.Five import schema
from immunarray.lims import messageFactory as _
from immunarray.lims.interfaces.solution import *
from plone import api
from zope.component import adapter
from zope.interface import Interface
from zope.interface import implementer
from plone.app.content.interfaces import INameFromTitle

def currentTime():
    return datetime.datetime.now()


def currentDate():
    return datetime.datetime.now().date()

def assignVeracisId():
    """Pull all Veracis IDs for R&D and QC samples and get the next one.
    """
    allVeracisIds = []
    qcsamples=[]
    randdsamples = []
    try:
        qcsamples = api.content.find(context=api.portal.get(), portal_type='QCSample')
    except:
        print "No QC samples found"
    if len(qcsamples) != 0:
        qc_sampel_uids = [u.UID for u in qcsamples]
        for i in qc_sampel_uids:
            record = api.content.get(UID=i)
            try:
                allVeracisIds.append(int(record.veracis_id))
            except:
                print "QC Veracis ID can't be converted to Int"
    # Get R&D Veracis ID's, append to allVeracisIds array
    try:
        randdsamples = api.content.find(context=api.portal.get(), portal_type='RandDSample')
    except:
        print "No R&D samples found"
    if len(randdsamples) != 0:
        randd_sampel_uids = [u.UID for u in randdsamples]
        for i in randd_sampel_uids:
            record = api.content.get(UID=i)
            try:
                allVeracisIds.append(int(record.veracis_id))
            except:
                print "R&D Veracis ID can't be converted to Int"
    # Now have a list of ints that are the veracis IDs of QC and R&D samples
    if len(allVeracisIds) !=0:
        next_veracis_id_int = max(allVeracisIds) + 1
        # Need to make the int into a unicode string
        next_veracis_id = str(next_veracis_id_int).encode("utf-8").decode("utf-8")
        return next_veracis_id
    else:
        next_veracis_id = str("1000").encode("utf-8").decode("utf-8")
        return next_veracis_id

class IQCSample(model.Schema):
    """QC Sample!
    """
    veracis_id = schema.TextLine(
        title=_(u"QC Veracis Sample ID"),
        description=_(u"QC Veracis Sample ID"),
        default=assignVeracisId(),
        required=True,
    )

    source_id_one = schema.TextLine(
        title=_(u"Primary QC Source Sample ID"),
        description=_(u"Primary QC Source Sample ID"),
        required=False,
    )

    source_id_two = schema.TextLine(
        title=_(u"Secondary QC Source Sample ID"),
        description=_(u"Secondary QC Source Sample ID"),
        required=False,
    )

    source_id_three = schema.TextLine(
        title=_(u"Tertiary QC Source Sample ID"),
        description=_(u"Tertiary QC Source Sample ID"),
        required=False,
    )

    commercial_use_status = schema.Choice(
        title=_(u"QC Commercial Use Status"),
        description=_(u"QC Commercial Use Status"),
        values=[_(u"Under Review"), _(u"Rejected"),  _(u"Released"), _(u"In Use"),_(u"Consumed")],
        required=True,
    )

    date_added = schema.Date(
        title=_(u"Date QC Sample was added to LIMS"),
        description=_(u"Date QC Sample was added to LIMS"),
        defaultFactory=currentDate,
        required=True,
    )

    added_by = schema.Choice(
        title=_(u"Operator that Added QC Sample to LIMS"),
        description=_(u"Operator that Added QC Sample to LIMS"),
        vocabulary=u"plone.principalsource.Users",
        required=False,
    )

    source = schema.TextLine(
        title=_(u"Source of QC Sample"),
        description=_(u"Source of QC Sample"),
        required=False,
    )

    description = schema.TextLine(
        title=_(u"Description of QC Sample"),
        description=_(u"Description of QC Sample"),
        required=False,
    )

    initial_volume = schema.Float(
        title=_(u"Volume of QC Sample in micro liters (uL)"),
        description=_(u"Volume of QC Sample in micro liters (uL)"),
        required=False,
    )

    fluid_type = schema.Choice(
        title=_(u"QC Fluid Type"),
        description=_(u"QC Fluid Type"),
        values=[_(u"Serum"), _(u"Plasma"), _(u"CSF"), _(u"Tissue")],
        required=True,
    )

    date_received = schema.Date(
        title=_(u"Date QC Sample was Received"),
        description=_(u"Date QC Sample was Received"),
        required=True,
    )

    comment = schema.Text(
        title=_(u"Any Notes or Comments About the QC Sample"),
        description=_(u"Any Notes or Comments About the QC Sample"),
        required=False,
    )

class ITitleFromVeracisIDAndSourceIDOne(Interface):
    """Marker interface to enable name from filename behavior"""


@implementer(INameFromTitle)
@adapter(ITitleFromVeracisIDAndSourceIDOne)
class TitleFromVeracisIDAndSourceIDOne(object):

    def __new__(cls, context):
        import pdb;pdb.set_trace()
        instance = super(TitleFromVeracisIDAndSourceIDOne, cls).__new__(cls)
        veracisid = getattr(context, 'veracis_id', None)
        simple_name =getattr(context, 'source_id_one', None)
        filename = simple_name + "--" + veracisid
        context.setTitle = filename
        instance.title = filename
        return instance

    def __init__(self, context):
        pass

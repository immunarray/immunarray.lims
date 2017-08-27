# -*- coding: utf-8 -*-
import datetime

from immunarray.lims import messageFactory as _
from immunarray.lims.interfaces.solution import *
from plone import api
from plone.app.content.interfaces import INameFromTitle
from zope import schema
from zope.component import adapter
from zope.interface import Interface, alsoProvides, implements
from zope.interface import implementer
from zope.schema.interfaces import IContextAwareDefaultFactory


def currentTime():
    return datetime.datetime.now()


def currentDate():
    return datetime.datetime.now().date()


class assignVeracisId():
    implements(IContextAwareDefaultFactory)

    def __init__(self):
        pass

    def __call__(self, context):
        """Pull all Veracis IDs for R&D and QC samples and get the next one.
        """
        brains = api.content.find(
            portal_type=['QCSample', 'RandDSample'], sort_on='veracis_id',
            sort_order='reverse', limit=1)
        if brains:
            _id = str(int(brains[0].veracis_id) + 1)
            return unicode(_id)
        print "No QC or RandD samples found"
        return u"1000"


class ITitleFromVeracisIDAndSourceIDOne(Interface):
    """Marker interface to enable name from filename behavior"""


@implementer(INameFromTitle)
@adapter(ITitleFromVeracisIDAndSourceIDOne)
class TitleFromVeracisIDAndSourceIDOne(object):
    def __new__(cls, context):
        instance = super(TitleFromVeracisIDAndSourceIDOne, cls).__new__(cls)
        veracisid = context.veracis_id
        simple_name = context.source_id_one
        filename = simple_name + "--" + veracisid
        context.setTitle(filename)
        instance.title = filename
        return instance

    def __init__(self, context):
        pass


class IQCSample(model.Schema):
    """QC Sample!
    """
    veracis_id = schema.TextLine(
        title=_(u"QC Veracis Sample ID"),
        description=_(u"QC Veracis Sample ID"),
        defaultFactory=assignVeracisId(),
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
        values=[_(u"Under Review"), _(u"Rejected"), _(u"Released"),
                _(u"In Use"), _(u"Consumed")],
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


alsoProvides(IQCSample, IFormFieldProvider)

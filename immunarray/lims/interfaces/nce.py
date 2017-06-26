# -*- coding: utf-8 -*-
"""To add custome slide content to immunarray.lims
"""
import datetime

from immunarray.lims import messageFactory as _
from plone.autoform import directives
from plone.supermodel import model
from zope import schema

def currentTime():
    return datetime.datetime.now()


class INCE(model.Schema):
    """General NCE Item to be used to track non conformance events in the lab
    """

    nce_tracking_number = schema.TextLine(
        title=_(u"Tracking Number"),
        description=_(u"Tracking Number"),
        required=False,
    )

    date_of_NCE = schema.Date(
        title=_(u"Date of NCE"),
        description=_(u"Date of NCE"),
        required=True,
    )

    date_of_nce_discovery = schema.Date(
        title=_(u"Date of NCE Discovery"),
        description=_(u"Date of NCE Discovery"),
        required=True,
    )
    
    reporter = schema.Choice(
        title=_(u"Operator that is Reporting NCE"),
        description=_(u"Operator that is Reporting NCE"),
        vocabulary=u"plone.principalsource.Users",
        required=False,
    )

    position = schema.TextLine(
        title=_(u"Position of Reporter"),
        description=_(u"Position of Reporter"),
        required=False,
    )

    area_of_operation = schema.Choice(
        title=_(u"Area of Operation"),
        description=_(u"Area of Operation"),
        values=[_(u'Scanning'),_(u'Accessioning'),_(u'Test Preparation'),_(u'Blocking'),_(u'Testing'),_(u'Data Analysis')],
        required=False,
    )

    accession_number = schema.TextLine(
        title=_(u"Accession Number or Batch Number"),
        description=_(u"Accession Number or Batch Number"),
        required=False,
    )

    assay = schema.TextLine(
        title=_(u"Assay"),
        description=_(u"Assay"),
        required=False,
    )

    facility = schema.TextLine(
        title=_(u"Facility where NCE Happened"),
        description=_(u"Facility where NCE Happened"),
        required=False,
    )

    current_date_time = schema.Datetime(
        title=_(u"Datetime of NCE"),
        description=_(u"Datetime of NCE"),
        defaultFactory=currentTime,
        required=True,
    )
    category_primary = schema.Choice(
        title=_(u"Category - Primary"),
        description=_(u"Category - Primary"),
        vocabulary='immunarray.lims.vocabularies.nce.PrimaryNCEVocabulary',
        required=False,
    )

    category_secondary = schema.Choice(
        title=_(u"Category - Secondary"),
        description=_(u"Category - Secondary"),
        vocabulary='immunarray.lims.vocabularies.nce.SecondaryNCEVocabulary',
        required=False,
    )

    category_tertiary = schema.Choice(
        title=_(u"Category - Tertiary"),
        description=_(u"Category - Tertiary"),
        vocabulary='immunarray.lims.vocabularies.nce.TertiaryNCEVocabulary',
        required=False,
    )
    risk_score = schema.Choice(
        title=_(u"Risk Score"),
        description=_(u"Risk Score"),
        values=[_(u'Lowest'),_(u'Intermediate'),_(u'High')],
        required=False,
    )
    initial_finding = schema.Text(
        title=_(u"Initial Finding"),
        description=_(u"Initial Finding"),
        required=False,
    )

    first_occurrence = schema.Bool(
        title=_(u"First Occurrence"),
        description=_(u"First Occurrence"),
        required=True,
        default=False,
    )

    persons_involved = schema.TextLine(
        title=_(u"Persons Involved"),
        description=_(u"Persons Involved"),
        required=False,
    )

    remedial_action_type = schema.Choice(
        title=_(u"Remedial Action Type"),
        description=_(u"Remedial Action Type"),
        values=[_(u'Corrective'),_(u'Preventive'),_(u'Process Improve')],
        required=False,
    )

    remedial_action = schema.Text(
        title=_(u"Remedial Action"),
        description=_(u"Remedial Action"),
        required=False,
    )

    is_follow_up_needed = schema.Bool(
        title=_(u"Is Follow Up Needed?"),
        description=_(u"Is Follow Up Needed?"),
        required=True,
        default=False,
    )

    investigation_needed = schema.Bool(
        title=_(u"Investigation Needed"),
        description=_(u"Investigation Needed"),
        required=True,
        default=False,
    )

    Investigation_tracking_number = schema.TextLine(
        title=_(u"Investigation Tracking Number"),
        description=_(u"Investigation Tracking Number"),
        required=False,
    )
    nce_status = schema.Choice(
        title=_(u"Status"),
        description=_(u"Status"),
        values=[_(u'Closed'),_(u'In Process'),_(u'Non Resolvable')],
        required=False,
    )
    date_closed = schema.Date(
        title=_(u"Date NCE Closed"),
        description=_(u"Date NCE Closed"),
        required=False,
    )

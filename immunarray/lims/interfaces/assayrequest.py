# -*- coding: utf-8 -*-
from zope import schema

import datetime
from immunarray.lims import messageFactory as _
from immunarray.lims.vocabularies.ichipassay import IChipAssayListVocabulary
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from immunarray.lims.interfaces import BaseModel
from zope.interface import alsoProvides


def currentDate():
    return datetime.datetime.now().date()


class IAssayRequest(BaseModel):
    """Object that will be attached to sample.  It will be the instance object
    that has a workflow that can be tracked in the LIMS.
    """
    assay_name = schema.Choice(
        title=_(u"Assay Name"),
        description=_(u"Assay Name"),
        source=IChipAssayListVocabulary,
        required=True,
    )

    date_ordered = schema.Date(
        title=_(u"Date Ordered"),
        description=_(u"Date Ordered"),
        defaultFactory=currentDate,
        required=True,
    )

    date_resulted = schema.Date(
        title=_(u"Assay Result Date"),
        description=_(u"Assay Result Date"),
        required=False,
    )

    aliquot_evaluated = schema.TextLine(
        title=_(u"Aliquot ID Used For Assay Request"),
        description=_(u"Aliquot ID Used For Assay Request"),
        required=False,
    )

    comment = schema.Text(
        title=_(u"Any Notes or Comments About the Assay Request"),
        description=_(u"Any Notes or Comments About the Assay Request"),
        required=False,
    )

alsoProvides(IAssayRequest, IFormFieldProvider)

# -*- coding: utf-8 -*-
from immunarray.lims import messageFactory as _
from immunarray.lims.interfaces import BaseModel
from plone.autoform.interfaces import IFormFieldProvider
from zope import schema
from zope.interface import alsoProvides


class ISolution(BaseModel):
    """Base Solution schema fields
    """

    title = schema.TextLine(
        title=_(u"Batch Number"),
        description=_(u"Batch number of solution"),
        required=True,
    )

    make_date = schema.Date(
        title=_(u"Date Made"),
        description=_(u"Date Solution was Made"),
        required=True,
    )

    expiration_date = schema.Date(
        title=_(u"Expiration Date"),
        description=_(u"Expiration Date"),
        required=True,
    )

    volume = schema.TextLine(
        title=_(u"Amount made"),
        description=_(u"Specify with SI units, eg: 2l, 2g, or 2kg"),
        required=True,
    )

    viability = schema.Int(
        title=_(u"Solution Viability"),
        description=_(u"Viability of solution in hours.  Leave blank if "
                      u"solution does not expire."),
        required=False,
    )

    status = schema.Choice(
        title=_(u"Status"),
        description=_(u"Release Status"),
        values=[_(u'Released'), _(u'Quarantened'), _(u'Consumed')],
        required=True,
    )


alsoProvides(ISolution, IFormFieldProvider)

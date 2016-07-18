# -*- coding: utf-8 -*-
from zope import schema

from zope.interface import alsoProvides

from immunarray.lims import messageFactory as _
from plone.autoform.interfaces import IFormFieldProvider
from plone.namedfile import field as namedfile
from plone.supermodel import model


class IMaterial(model.Schema):
    """Base schema fields common to all Material types.

    To use these fields, create a new Dexterity type and enable the
    IMaterial behaviour for it.
    """
    LotNumber = schema.TextLine(
        title=_(u"Lot"),
        description=_(u"The lot number"),
        required=True
    )
    Vendor = schema.TextLine(
        title=_(u"Vendor"),
        description=_(u"The vendor that supplied the lot"),
        required=True
    )
    CatalogNumber = schema.TextLine(
        title=_(u"Catalog Number"),
        description=_(u"The lot's catalog number"),
        required=True
    )
    ArrivalDate = schema.Date(
        title=_(u"Arrival Date"),
        description=_(u"The date on which the lot arrived"),
        required=True
    )
    ExpirationDate = schema.Date(
        title=_(u"Expiration Date"),
        description=_(
            u"The date on which the lot expires"),
        required=True
    )
    COA = namedfile.NamedBlobImage(
        title=_(u"Certificate of Analysis"),
        description=_(u"Certificate of Analysis"),
        required=True
    )
    ArrivalAmount = schema.TextLine(
        title=_(u"Amount of material at time of arrival"),
        description=_(u"Specify with SI units, eg: 1uL, 1', 20g, or 1 kg."),
        required=True,
    )
    CurrentAmount = schema.TextLine(
        title=_(u"Amount of material currently remaining"),
        description=_(u"Specify with SI units, eg: 1uL, 1', 20g, or 1 kg."),
        required=False
    )
    ReceivedBy = schema.Choice(
        title=_(u"Received by"),
        description=_(u"The operator that received the material lot"),
        vocabulary=u"plone.principalsource.Users",
        required=False  # value will be completed by workflow transition
    )
    OpenedBy = schema.Choice(
        title=_(u"Opened by"),
        description=_(u"The operator that Opened the material lot"),
        vocabulary=u"plone.principalsource.Users",
        required=False  # value will be completed by workflow transition
    )


alsoProvides(IMaterial, IFormFieldProvider)

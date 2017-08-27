# -*- coding: utf-8 -*-
from immunarray.lims import messageFactory as _
from plone.app.content.interfaces import INameFromTitle
from plone.autoform.interfaces import IFormFieldProvider
from plone.namedfile.field import NamedBlobImage
from plone.supermodel import model
from zope import schema
from zope.component import adapter
from zope.interface import Interface
from zope.interface import alsoProvides
from zope.interface import implementer


class IMaterial(model.Schema):
    """Base schema fields common to all Material types.

    To use these fields, create a new Dexterity type and enable the
    IMaterial behaviour for it.
    """

    lot_number = schema.TextLine(
        title=_(u"Lot"),
        description=_(u"The lot number"),
        required=True
    )

    vendor = schema.TextLine(
        title=_(u"Vendor"),
        description=_(u"The vendor that supplied the lot"),
        required=True
    )

    catalog_number = schema.TextLine(
        title=_(u"Catalog Number"),
        description=_(u"The lot's catalog number"),
        required=True
    )

    arrival_date = schema.Date(
        title=_(u"Arrival Date"),
        description=_(u"The date on which the lot arrived"),
        required=True
    )

    expiration_date = schema.Date(
        title=_(u"Expiration Date"),
        description=_(
            u"The date on which the lot expires"),
        required=True
    )

    coa = NamedBlobImage(
        title=_(u"Certificate of Analysis"),
        description=_(u"Certificate of Analysis"),
        required=False
    )

    arrival_amount = schema.TextLine(
        title=_(u"Amount of material at time of arrival"),
        description=_(u"Specify with SI units, eg: 1uL, 1', 20g, or 1 kg."),
        required=True,
    )

    current_amount = schema.TextLine(
        title=_(u"Amount of material currently remaining"),
        description=_(u"Specify with SI units, eg: 1uL, 1', 20g, or 1 kg."),
        required=False
    )

    received_by = schema.Choice(
        title=_(u"Received by"),
        description=_(u"The operator that received the material lot"),
        vocabulary=u"plone.principalsource.Users",
        required=False  # value will be completed by workflow transition
    )

    opened_by = schema.Choice(
        title=_(u"Opened by"),
        description=_(u"The operator that Opened the material lot"),
        vocabulary=u"plone.principalsource.Users",
        required=False  # value will be completed by workflow transition
    )

    product_name = schema.TextLine(
        title=_(u"Product Name"),
        description=_(u"Product Name"),
        required=True
    )
    purchase_order = schema.TextLine(
        title=_(u"Purchase Order"),
        description=_(u"Purchase Order"),
        required=False
    )
    shipping_tracking_number = schema.TextLine(
        title=_(u"Shipping Tracking Number"),
        description=_(u"Shipping Tracking Number"),
        required=False
    )

    intended_use = schema.Choice(
        title=_(u"Intended Use"),
        description=_(u"Intended Use"),
        values=[_(u'Commercial'), _(u'Development')],
        required=True,
    )

    meets_raw_material_specifications = schema.Choice(
        title=_(u"Meets Raw Material Specifications"),
        description=_(u"Meets Raw Material Specifications"),
        values=[_(u'Yes'), _(u'No')],
        required=False,
    )

    shipping_box_integrity_maintained = schema.Choice(
        title=_(u"Raw Materail Box Integrity Maintained"),
        description=_(u"Raw Material Box Integrity Maintained"),
        values=[_(u"Yes"), _(u"No")],
        required=False,
    )

    product_container_integrity_maintained = schema.Choice(
        title=_(u"Product Container Integrity Maintained"),
        description=_(u"Product Container Integrity Maintained"),
        values=[_(u"Yes"), _(u"No")],
        required=False,
    )

    other_damage = schema.TextLine(
        title=_(u"Other Damage"),
        description=_(u"Other Damage"),
        required=False,
    )

    temp_on_arrival = schema.TextLine(
        title=_(u"Temperature of Raw Material on Arrival"),
        description=_(u"Temperature of Raw Material on Arrival"),
        required=False,
    )

    temp_on_arrival_acceptable_limit = schema.Choice(
        title=_(
            u"Temerature of Raw Material on Arrival Within Acceptable Limit"),
        description=_(
            u"Temerature of Raw Materail on Arrival Within Acceptable Limit"),
        values=[_(u"Yes"), _(u"No")],
        required=False,
    )


alsoProvides(IMaterial, IFormFieldProvider)


class ITitleFromLotAndType(Interface):
    """Marker interface to enable name from filename behavior"""


@implementer(INameFromTitle)
@adapter(ITitleFromLotAndType)
class TitleFromLotAndType(object):
    def __new__(cls, context):
        instance = super(TitleFromLotAndType, cls).__new__(cls)
        lotnumber = getattr(context, 'lot_number', None)
        name = getattr(context, 'product_name', None)
        filename = name + "--" + lotnumber
        context.setTitle(filename)
        instance.title = filename
        return instance

    def __init__(self, context):
        pass

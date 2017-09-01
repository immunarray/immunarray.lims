# -*- coding: utf-8 -*-
from immunarray.lims import messageFactory as _
from immunarray.lims.fields.amount import Amount
from immunarray.lims.interfaces import BaseModel
from plone.autoform.interfaces import IFormFieldProvider
from plone.namedfile.field import NamedBlobImage
from zope import schema
from zope.interface import alsoProvides


class IMaterial(BaseModel):
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

    initial_amount = Amount(
        title=_(u"Initial amount made"),
        description=_(u"Enter a decimal number"),
        required=True,
    )

    remaining_amount = Amount(
        title=_(u"Amount remaining"),
        description=_(u"You should not need to edit this value"),
        readonly=True,
    )

    unit = schema.TextLine(
        title=_(u"Unit"),
        description=_("Enter the unit in which the amounts are measured"),
        required=True,
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

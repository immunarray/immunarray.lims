# -*- coding: utf-8 -*-
from immunarray.lims import messageFactory as _
from immunarray.lims.interfaces import BaseModel
from immunarray.lims.vocabularies.ichipassay import IChipAssayListVocabulary
from plone.autoform import directives as form
from plone.namedfile.field import NamedFile
from z3c.form.browser.checkbox import CheckBoxFieldWidget
from zope import schema
from zope.interface import Invalid


def NonZeroConstraint(value):
    """Check that the Int field has a value >0
    """
    try:
        int(value)
    except:
        raise Invalid(_(u"Value must be an integer, not '%s'" % value))
    if value < 1:
        raise Invalid(_(u"Value must be >0, not '%s'" % value))
    return True


class IiChipLot(BaseModel):
    """An iChip Lot that will contain iChip objects.
    """

    lot_id = schema.TextLine(
        title=_(u"iChip Lot ID"),
        description=_(u"Used when naming iChips created in this lot"),
        required=True,
    )

    print_date = schema.Date(
        title=_(u"iChip Lot Print Date"),
        description=_(u"Print Date of iChip Lot"),
        required=True,
    )

    arrival_date = schema.Date(
        title=_(u"iChip Lot Arrival Date"),
        description=_(u"Arrival Date of iChip Lot"),
        required=True,
    )

    ship_date = schema.Date(
        title=_(u"iChip Lot Shipped Date"),
        description=_(u"iChip Lot Shipped Date"),
        required=True,
    )

    ichip_lot_expiration_date = schema.Date(
        title=_(u"iChip Lot Expiration Date"),
        description=_(u"Expiration Date of iChip Lot"),
        required=True,
    )

    nr_ichips = schema.Int(
        title=_(u"Number of iChips"),
        description=_(u"Number of iChips contained in this lot."),
        required=True,
        constraint=NonZeroConstraint,
    )

    # XXX This should be a Text input, same as iChipAssay's framecount
    # and the two should match: refactor ichip.I*ChipsInUSVocabulary
    frames = schema.Choice(
        title=_(u"iChip Frame Layout"),
        description=_(u"iChip Frame Layout"),
        values=[_(u"1"), _(u"3"), _(u"8")],
        required=True,
    )
    # XXX Allow mutiple selections!
    # XXX Need to connect this to iChipAssay.name
    form.widget(intended_assay=CheckBoxFieldWidget)
    intended_assay = schema.List(
        title=_(u"Intended Assay(s)"),
        description=_(u"Intended Assay(s)"),
        required=True,
        value_type=schema.Choice(source=IChipAssayListVocabulary),
    )

    temp_log = NamedFile(
        title=_(u"iChip Lot Travel Temperature Log"),
        description=_(u"Travel Temperature Log of iChip Lot"),
        required=False,
    )

    cofa = NamedFile(
        title=_(u"iChip Certificate of Analysis"),
        description=_(u"Certificate of Analysis of iChip Lot"),
        required=False,
    )

    batch_release = NamedFile(
        title=_(u"iChip Batch Release Document"),
        description=_(u"Batch Release Document of iChip Lot"),
        required=False,
    )

    gal_file = NamedFile(
        title=_(u"Gal File (.gal)"),
        description=_(u"Gal File (.gal)"),
        required=False,
    )

    shipping_box_integrity_maintained = schema.Choice(
        title=_(u"iChip Shipping Box Integrity Maintained"),
        description=_(u"iChip Shipping Box Integrity Maintained"),
        values=[_(u"Yes"), _(u"No")],
        required=True,
    )

    product_container_integrity_maintained = schema.Choice(
        title=_(u"Product Container Integrity Maintained"),
        description=_(u"Product Container Integrity Maintained"),
        values=[_(u"Yes"), _(u"No")],
        required=True,
    )

    other_damage = schema.TextLine(
        title=_(u"Other Damage"),
        description=_(u"Other Damage"),
        required=False,
    )

    temp_on_arrival = schema.Float(
        title=_(u"Temperature of iChips on Arrival"),
        description=_(u"Temperature of iChips on Arrival"),
        required=False,
    )

    temp_on_arrival_acceptable_limit = schema.Choice(
        title=_(u"Temperature of iChips on Arrival Within Acceptable Limit"),
        description=_(
            u"Temperature of iChips on Arrival Within Acceptable Limit"),
        values=[_(u"Yes"), _(u"No")],
        required=True,
    )

from immunarray.lims import messageFactory as _
from plone.namedfile.field import NamedFile
from plone.supermodel import model
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


class IiChipLot(model.Schema):
    """An iChip Lot that will contain iChip objects.
    """

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

    expiration_date = schema.Date(
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

    frames = schema.Choice(
        title=_(u"iChip frames"),
        description=_(u"The type of ichips that are contained here"),
        values=[_(u"No Frame iChips"),
                _(u"3 Frame iChips"),
                _(u"8 Frame iChips")],
        required=True,
    )

    temp_log = NamedFile(
        title=_(u"iChip Lot Travel Temperature Log"),
        description=_(u"Travel Temperature Log of iChip Lot"),
        required=False,
    )

    acceptance_status = schema.Choice(
        title=_(u"iChip Acceptance Status"),
        description=_(u"Acceptance Status of iChip Lot"),
        values=[_(u"Quarantined"), _(u"Passed")],
        required=True,
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

    temp_on_arrival = schema.TextLine(
        title=_(u"Temperature of iChips on Arrival"),
        description=_(u"Temperature of iChips on Arrival"),
        required=False,
    )

    temp_on_arrival_acceptable_limit = schema.Choice(
        title=_(u"Temerature of iChips on Arrival Within Acceptable Limit"),
        description=_(u"Temerature of iChips on Arrival Within Acceptable Limit"),
        values=[_(u"Yes"), _(u"No")],
        required=True,
    )

from zope import schema

from Products.CMFCore.utils import getToolByName
from plone.supermodel import model
from plone.uuid.interfaces import IUUID
from z3c.form import validator
from zope.interface import Invalid

from immunarray.lims import messageFactory as _


class IiChipLot(model.Schema):
    """An iChip Lot that will contain iChip objects.
    """

    ichiplotID = schema.TextLine(
        title=_(u"iChip Lot ID"),
        description=_(u"iChip Lot ID"),
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

    expiration_date = schema.Date(
        title=_(u"iChip Lot Expiration Date"),
        description=_(u"Expiration Date of iChip Lot"),
        required=True,
    )

    framecount = schema.Choice(
        title=_(u"iChip frames"),
        description=_(u"The type of ichips that are contained here"),
        values=[_(u"No Frame iChips"), _(u"3 Frame iChips"), _(u"8 Frame iChips")],
        required=True,
    )

    temp_log = schema.Bytes(
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

    cofa = schema.Bytes(
        title=_(u"iChip Certificate of Analysis"),
        description=_(u"Certificate of Analysis of iChip Lot"),
        required=False,
    )

    batch_release = schema.Bytes(
        title=_(u"iChip Batch Release Document"),
        description=_(u"Batch Release Document of iChip Lot"),
        required=False,
    )

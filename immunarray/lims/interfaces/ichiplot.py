from plone.supermodel import model
from plone.uuid.interfaces import IUUID
from Products.CMFCore.utils import getToolByName
from z3c.form import validator
from zope import schema
from zope.interface import Invalid

from immunarray.lims import messageFactory as _

class IiChipLot(model.Schema):
    """An iChip Lot that will contain iChip objects.
    """

    # iChipLotCode = schema.TextLine(
    #         title=_(u"iChip Lot Code"),
    #         description=_(u"Code that could be use for external database longterm"),
    #         constraint=iChipLotCodeIsValid,
    #         )

    iChipLotID = schema.TextLine(
        title=_(u"iChip Lot ID"),
        description=_(u"ID of iChip Lot"),
        required=True,
    )
    iChipLotPrintDate = schema.Date(
        title=_(u"iChip Lot Print Date"),
        description=_(u"Print Date of iChip Lot"),
        required=True,
    )
    iChipLotArrivalDate = schema.Date(
        title=_(u"iChip Lot Arrival Date"),
        description=_(u"Arrival Date of iChip Lot"),
        required=True,
    )
    iChipLotExpDate = schema.Date(
        title=_(u"iChip Lot Expiration Date"),
        description=_(u"Expiration Date of iChip Lot"),
        required=True,
    )
    iChipLotTempLot = schema.Bytes(
        title=_(u"iChip Lot Travel Temperature Log"),
        description=_(u"Travel Temperature Log of iChip Lot"),
        required=False,
    )
    iChipLotAcceptanceStatus = schema.Choice(
        title=_(u"iChip Acceptance Status"),
        description=_(u"Acceptance Status of iChip Lot"),
        values=[_(u"Quarantined"), _(u"Passed")],
        required=True,
    )
    iChipLotCofA = schema.Bytes(
        title=_(u"iChip Certificate of Analysis"),
        description=_(u"Certificate of Analysis of iChip Lot"),
        required=False,
    )
    iChipLotBatchRelease = schema.Bytes(
        title=_(u"iChip Batch Release Document"),
        description=_(u"Batch Release Document of iChip Lot"),
        required=False,
    )


class ValidateiChipLotUniqueness(validator.SimpleFieldValidator):
    """Validate fuction to ensure that the iChip Lot ID is unique on add/edit
    """

    def validate(self, value):
        super(ValidateiChipLotUniqueness, self).validate(value)
        if value is not None:
            catalog = getToolByName(self.context, 'portal_catalog')
            results = catalog(
                {'iChipLotID': value, 'object_provides': iChip.__identifier__})

            contextUUID = IUUID(self.context, None)
            for result in results:
                if result.UID != contextUUID:
                    raise Invalid(_(u"The iChip Lot is already in assigned"))


validator.WidgetValidatorDiscriminators(
    ValidateiChipLotUniqueness,
    field=IiChipLot['iChipLotID'],
)

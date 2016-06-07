from plone.supermodel import model
from plone.uuid.interfaces import IUUID
from Products.CMFCore.utils import getToolByName
from z3c.form import validator
from zope import schema
from zope.interface import Invalid

from immunarray.lims import _

class IIChipLot(model.Schema):
    """An IChip Lot that will contain IChip objects.
    """

    # IChipLotCode = schema.ASCIILine(
    #         title=_(u"IChip Lot Code"),
    #         description=_(u"Code that could be use for external database longterm"),
    #         constraint=IChipLotCodeIsValid,
    #         )

    IChipLotID = schema.ASCIILine(
        title=_(u"IChip Lot ID"),
        description=_(u"ID of IChip Lot"),
        required=True,
    )
    IChipLotPrintDate = schema.Date(
        title=_(u"IChip Lot Print Date"),
        description=_(u"Print Date of IChip Lot"),
        required=True,
    )
    IChipLotArrivalDate = schema.Date(
        title=_(u"IChip Lot Arrival Date"),
        description=_(u"Arrival Date of IChip Lot"),
        required=True,
    )
    IChipLotExpDate = schema.Date(
        title=_(u"IChip Lot Expiration Date"),
        description=_(u"Expiration Date of IChip Lot"),
        required=True,
    )
    IChipLotTempLot = schema.Bytes(
        title=_(u"IChip Lot Travel Temperature Log"),
        description=_(u"Travle Temperature Log of IChip Lot"),
        required=False,
    )
    IChipLotAcceptanceStatus = schema.Choice(
        title=_(u"IChip Acceptance Status"),
        description=_(u"Acceptance Status of IChip Lot"),
        values=[_(u"Quarantined"), _(u"Passed")],
        required=True,
    )
    IChipLotCofA = schema.Bytes(
        title=_(u"IChip Certificate of Analysis"),
        description=_(u"Certificate of Analysis of IChip Lot"),
        required=False,
    )
    IChipLotBatchRelease = schema.Bytes(
        title=_(u"IChip Batch Release Document"),
        description=_(u"Batch Release Document of IChip Lot"),
        required=False,
    )


class ValidateIChipLotUniqueness(validator.SimpleFieldValidator):
    """Validate fuction to ensure that the IChip Lot ID is unique on add/edit
    """

    def validate(self, value):
        super(ValidateIChipLotUniqueness, self).validate(value)
        if value is not None:
            catalog = getToolByName(self.context, 'portal_catalog')
            results = catalog(
                {'IChipLotID': value, 'object_provides': IChip.__identifier__})

            contextUUID = IUUID(self.context, None)
            for result in results:
                if result.UID != contextUUID:
                    raise Invalid(_(u"The IChip Lot is already in assigned"))


validator.WidgetValidatorDiscriminators(
    ValidateIChipLotUniqueness,
    field=IIChipLot['IChipLotID'],
)

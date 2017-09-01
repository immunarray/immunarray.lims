# -*- coding: utf-8 -*-
from decimal import Decimal as D, InvalidOperation

from zope.schema import Decimal, ValidationError
from zope.schema.interfaces import IDecimal


class IAmount(IDecimal):
    """Field containing a unicode string representing a Magnitude value.
    """


class DecimalRequired(ValidationError):
    __doc__ = "A decimal value is required."


class NonNegativeValueRequired(ValidationError):
    __doc__ = "A non-negative value is required."


class Amount(Decimal):
    def validate(self, value):

        if value:
            try:
                D(value)
            except InvalidOperation:
                raise DecimalRequired
            if value < 0:
                raise NonNegativeValueRequired

        return super(Amount, self).validate(value)

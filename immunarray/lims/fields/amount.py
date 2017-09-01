# -*- coding: utf-8 -*-
from zope.schema import Float, ValidationError
from zope.schema.interfaces import IFloat


class IAmount(IFloat):
    """Field containing a unicode string representing a Magnitude value.
    """


class DecimalRequired(ValidationError):
    __doc__ = "A decimal value is required."


class NonNegativeValueRequired(ValidationError):
    __doc__ = "A non-negative value is required."


class Amount(Float):
    def validate(self, value):

        if value:
            try:
                float(value)
            except (TypeError, ValueError):
                raise DecimalRequired
            if value < 0:
                raise NonNegativeValueRequired

        return super(Amount, self).validate(value)

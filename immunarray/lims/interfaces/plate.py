from zope import schema
from zope.interface import Interface

from immunarray.lims import messageFactory as _
from plone.supermodel import model


class IPlate96Well(model.Schema):
    """
    A 96 Well plate object
    """

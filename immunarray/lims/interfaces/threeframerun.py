from datetime import date
from immunarray.lims.interfaces.veracisrunbase import IVeracisRunBase
from immunarray.lims import messageFactory as _
from plone.app.textfield import RichText
from plone.supermodel import model
from zope import schema

class IThreeFrameRun(IVeracisRunBase):
    aliquot_to_well = schema.Dict(
        key_type=schema.TextLine(title=u"Aliquot ID"),
        value_type=schema.TextLine(title=u"iChip and Well ID V6.1_33-1")
    )

from datetime import date
from immunarray.lims.interfaces import veracisrunbase
from immunarray.lims import messageFactory as _
from plone.app.textfield import RichText
from plone.namedfile.field import NamedBlobImage
from plone.supermodel import model
from zope import schema

class IThreeFrameRun(IVeracisRunBase):
    pass
    status = schema.Dict(
        key_type=schema.TextLine(title=u""),
        values_type=schema.TextLine(title=u"iChip_ID")
    )

# -*- coding: utf-8 -*-
from datetime import date
from immunarray.lims.interfaces.veracisrunbase import IVeracisRunBase
from immunarray.lims import messageFactory as _
from plone.app.textfield import RichText
from plone.supermodel import model
from zope import schema

class INoFrameRun(IVeracisRunBase):
    status = schema.Dict(
        key_type=schema.TextLine(title=u""),
        value_type=schema.TextLine(title=u"iChip_ID")
    )

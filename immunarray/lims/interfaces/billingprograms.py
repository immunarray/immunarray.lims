# -*- coding: utf-8 -*-
import datetime
from zope import schema

class IAssayRequest(model.Schema):
    """Object that will be billing programs that can be added to the system,
    will be what is used to determin if a billing message needs to be generated,
    cost to patient, and message structure to be sent to third party.
    """

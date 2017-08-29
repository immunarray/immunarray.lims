# -*- extra stuff goes here -*-
from AccessControl import allow_module
from zope.i18nmessageid import MessageFactory
import logging

messageFactory = MessageFactory('Immunarray')

# import this to log messages
logger = logging.getLogger('Immunarray')


def initialize(context):
    """Initializer called when used as a Zope 2 product."""

allow_module('immunarray.lims.workflow')

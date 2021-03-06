# -*- extra stuff goes here -*-
from AccessControl import allow_module
from plone.i18n.normalizer import IIDNormalizer
from zope.component import queryUtility
from zope.i18nmessageid import MessageFactory
import logging

messageFactory = MessageFactory('Immunarray')

# import this to log messages
logger = logging.getLogger('Immunarray')


def normalize(value):
    """Normalize a value to UPPERCASE
    """
    normalizer = queryUtility(IIDNormalizer)
    return normalizer.normalize(value).upper()


def initialize(context):
    """Initializer called when used as a Zope 2 product."""

allow_module('immunarray.lims.workflow')

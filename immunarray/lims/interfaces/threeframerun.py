# -*- coding: utf-8 -*-
from datetime import date
from immunarray.lims.interfaces.veracisrunbase import IVeracisRunBase
from immunarray.lims import messageFactory as _
from plone.app.textfield import RichText
from plone.supermodel import model
from zope import schema
from plone.autoform.interfaces import IFormFieldProvider
from immunarray.lims.vocabularies.ichip import *
from immunarray.lims.vocabularies import ichip
from immunarray.lims.vocabularies.ichipassay import IChipAssayListVocabulary
from immunarray.lims.vocabularies import ichipassay
from immunarray.lims.vocabularies.provider import ProvidersVocabulary
from z3c.relationfield import RelationChoice
from plone.directives import form
from plone import api
from plone.i18n.normalizer.interfaces import IIDNormalizer
from zope.component import queryUtility
from zope.interface import implements, Interface, implementer
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.interfaces import IContextSourceBinder
from Products.CMFCore.interfaces import IContentish
from Products.CMFCore.utils import getToolByName
from zope.interface import alsoProvides
from plone.app.z3cform.widget import *
from plone.autoform import directives
from z3c.form import form, button

class IThreeFrameRun(IVeracisRunBase):

    aliquot_to_well = schema.Dict(
        key_type=schema.TextLine(title=u"Aliquot ID", required=False),
        value_type=schema.Choice(source=ICommercailThreeFrameChipWellsVocabulary, required=False)
    )

    ten_x_pbs = schema.TextLine(
        title=_(u"10X PBS Lot Used"),
        description=_(u"10X PBS Lot Used"),
        required=False,
    )

    one_x_pbs = schema.TextLine(
        title=_(u"1X PBS Lot Used"),
        description=_(u"1X PBS Lot Used"),
        required=False,
    )

    one_x_pbs_22_tween20 = schema.TextLine(
        title=_(u"1X PBS - 22% Tween 20 Lot Used"),
        description=_(u"1X PBS - 22% Tween 20 Lot Used"),
        required=False,
    )
alsoProvides(IThreeFrameRun, IFormFieldProvider)


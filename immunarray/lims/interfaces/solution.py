# -*- coding: utf-8 -*-
from zope import schema

from zope.interface import alsoProvides

from immunarray.lims import messageFactory as _
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model


class ISolution(model.Schema):
    SolutionID = schema.Int(
        title=_(u"Batch Number"),
        description=_(u"Batch number of solution"),
        required=True,
    )
    SolutionExpDate = schema.Date(
        title=_(u"Expiration Date"),
        description=_(u"Expiration Date"),
        required=True,
    )
    SolutionMakeDate = schema.Date(
        title=_(u"Date Made"),
        description=_(u"Date Solution was Made"),
        required=True,
    )
    SolutionVolume = schema.Int(
        title=_(u"Amount made"),
        description=_(u"Specify with SI units, eg: 2l, 2g, or 2kg"),
        required=True,
    )
    SolutionViability = schema.Int(
        title=_(u"Solution Viability"),
        description=_(u"Viability of solution in hours.  Leave blank if "
                      u"solution does not expire."),
        required=False,
    )
    PBS1xStatus = schema.Choice(
        title=_(u"Status"),
        description=_(u"Release Status"),
        values=[_(u'Released'), _(u'Quarantened'), _(u'Consumed')],
        required=True,
    )


alsoProvides(ISolution, IFormFieldProvider)


class I1xpbs(model.Schema):
    PBS1xBatchof10xpbs = schema.Choice(
        title=_(u"Batch of 10 x PBS Used"),
        description=_(u"Batch of 10 x Used"),
        vocabulary="immunarray.lims.interfaces.vocabulary.PBS10xlotVocabulary",
        required=False,
    )
    PBS1xVolumeof10xpbsAdded = schema.Float(
        title=_(u"Volume of 10x PBS"),
        description=_(u"Volume of 10X PBS Added Liters"),
        required=False,
    )
    PBS1xVolumeofWaterAdded = schema.Float(
        title=_(u"Water Added to 10x PBS"),
        description=_(u"Water Added to 10xPBS in Liters"),
        required=False,
    )
    PBS1xVerifypHMeter = schema.Float(
        title=_(u"Water Added to 10x PBS"),
        description=_(u"Water Added to 10xPBS in Liters"),
        required=False,
    )
    PBS1xpH = schema.Float(
        title=_(u"Observed pH of 1 x PBS"),
        description=_(u"Observed pH of 1 x PBS"),
        required=False,
    )


class I10xpbs(model.Schema):
    PBS10xVolumeofWaterAdded = schema.Float(
        title=_(u"Water Added to 10x PBS"),
        description=_(u"Water Added to 10xPBS in Liters"),
        required=False,
    )
    PBS10xSodiumChlorideLotAdded = schema.Choice(
        title=_(u"Lot of Sodium Chloride Added to PBS (10X)"),
        description=_(u"Lot of Sodium Chloride PBS (10X)"),
        vocabulary="immunarray.lims.interfaces.vocabulary.SodiumChlorideVocabulary",
        required=False,
    )
    PBS10xMassSodiumChlorideAdded = schema.Float(
        title=_(u"Mass of Sodium Chloride Added to PBS (10X)"),
        description=_(u"Mass of Sodium Chloride PBS (10X)"),
        required=False,
    )
    PBS10xPotassiumChlorideLotAdded = schema.Choice(
        title=_(u"Lot of Potassium Chloride Added to PBS (10X)"),
        description=_(u"Lot of Potassium Chloride PBS (10X)"),
        vocabulary="immunarray.lims.interfaces.vocabulary.PotassiumChlorideVocabulary",
        required=False,
    )
    PBS10xMassPotassiumChlorideAdded = schema.Float(
        title=_(u"Mass of Potassium Chloride Added to PBS (10X)"),
        description=_(u"Mass of Potassium Chloride PBS (10X)"),
        required=False,
    )
    PBS10xLotSodiumPhosphatedibasicAdded = schema.Choice(
        title=_(u"Lot of Sodium Phosphate Dibasic Added to PBS (10X)"),
        description=_(u"Lot of Sodium Phosphate Dibasic PBS (10X)"),
        vocabulary="immunarray.lims.interfaces.vocabulary.SodiumPhosphatedibasicVocabulary",
        required=False,
    )
    PBS10xMassSodiumPhosphatedibasicAdded = schema.Float(
        title=_(u"Mass of Sodium Phosphate Dibasic Added to PBS (10X)"),
        description=_(u"Mass of Potassium Chloride PBS (10X)"),
        required=False,
    )
    PBS10xLotPotassiumPhosphatemonobasicAdded = schema.Choice(
        title=_(u"Lot of Sodium Phosphate Dibasic Added to PBS (10X)"),
        description=_(u"Lot of Sodium Phosphate Dibasic PBS (10X)"),
        vocabulary="immunarray.lims.interfaces.vocabulary.PotassiumPhosphatemonobasicVocabulary",
        required=False,
    )
    PBS10xMassPotassiumPhosphatemonobasicAdded = schema.Float(
        title=_(u"Mass of Potassium Phosphate Monobasic Added to PBS (10X)"),
        description=_(u"Mass of Potassium Phosphate Monobasic PBS (10X)"),
        required=False,
    )
    PBS10xVerifypHMeter = schema.Float(
        title=_(u"Measured pH of PBS (10X)"),
        description=_(u"pH of PBS (10X)"),
        required=False,
    )
    PBS10xpH = schema.Float(
        title=_(u"Observed pH of 10 x PBS Post HCl or NaOH Addition"),
        description=_(u"Observed pH of 10 x PBS Post HCl or NaOH Addition"),
        required=False,
    )


class I1PercentCasein(model.Schema):
    OnePercentCaseinLotofCaseinSalt = schema.Choice(
        title=_(u"Lot of Casein Salt Used"),
        description=_(u"Lot of Casein Salt Used"),
        vocabulary="immunarray.lims.interfaces.vocabulary.CaseinSaltVocabulary",
        required=False,
    )
    OnePercentCaseinLot1xpbs = schema.Choice(
        title=_(u"Lot of PBS (1X) Used"),
        description=_(u"Lot of PBS (1X) Used"),
        vocabulary="immunarray.lims.interfaces.vocabulary.PBS1xlotVocabulary",
        required=False,
    )
    OnePercentCaseinAdded = schema.Float(
        title=_(u"Mass of Casein Salt Added"),
        description=_(u"Mass of Casein Salt Added to PBS"),
        required=False,
    )
    OnePercentCasein1xPBSAdded = schema.Float(
        title=_(u"Volume of 1 x PBS Added"),
        description=_(u"Volume of 1 x PBS Added to Casein Salt"),
        required=False,
    )


class I70PercentEthyanol(model.Schema):
    SeventyPercentEthyanolVolumeEthanol = schema.Float(
        title=_(u"Volume of Ethanol Added"),
        description=_(u"Volume of Ethanol Added"),
        required=False,
    )
    SeventyPercentEthyanolVolumeWater = schema.Float(
        title=_(u"Volume of Water Added"),
        description=_(u"Volume of Water Added"),
        required=False,
    )


class ITween22_4Percentinpbs(model.Schema):
    pass

class I1mgpermlIgg_cy3(model.Schema):
    pass


class I1mgpermlIgm_af647(model.Schema):
    pass


class I3Mkcl(model.Schema):
    pass


class I50PercentGlycerol(model.Schema):
    pass


class I10Percenthcl(model.Schema):
    pass


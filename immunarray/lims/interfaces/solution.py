from zope import schema

from immunarray.lims import messageFactory as _
from plone.supermodel import model


class ISolution(model.Schema):
    SolutionType = schema.Choice(
            title=_(u"Type of Solution"),
            description=_(u"Type of Solution"),
            values=[_(u"1xPBS"),\
                   _(u"1%Casein in PBS"),\
                   _(u"Secondary Antibody"),\
                   _(u"10xPBS"),\
                   _(u"70% Ethylalchol (Cleaning Solution)"),\
                   _(u"22.4% Tween in 1xPBS"),\
                   _(u"3M KCl"),\
                   _(u"10% HCl"),\
                   _(u"50% Glycerol"),\
                   _(u"1mg/mL IgG-Cy3 in 50% Glycerol"),\
                   _(u"1mg/mL IgM-AF647 in 50% Glycerol")],
            required=True,
            )
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
            description=_(u"Data Solution was Made"),
            required=True,
            )
    SolutionViability = schema.Int(
            title=_(u"Solution Viability"),
            description=_(u"Viability of solution in hours"),
            required=False,
            )
    SolutionVolume = schema.Int(
            title=_(u"Solution Volume"),
            description=_(u"Volume of solution"),
            required=False,
            )
class I1xpbs(model.Schema):
    PBS1xBatch = schema.Int(
            title=_(u"Batch Number"),
            description=_(u"Batch number of solution"),
            required=True,
            )
    PBS1xTotalVolume = schema.Choice(
            title=_(u"Solution Volume"),
            description=_(u"Volume of solution"),
            values =[_(u"10L"),\
                   _(u"7L"),\
                   _(u"5L")], 
            required=True,
            )
    PBS1xMakeDate = schema.Date(
            title=_(u"Date Made"),
            description=_(u"Data Solution was Made"),
            required=True,
            )
    PBS1xExpDate = schema.Date(
            title=_(u"Expiration Date"),
            description=_(u"Expiration Date"),
            required=True,
            )
    PBS1xViability = schema.Int(
            title=_(u"Solution Viability"),
            description=_(u"Viability of solution in hours"),
            required=False,
            )
    PBS1xStatus = schema.Choice(
            title=_(u"Status"),
            description=_(u"PBS (1X) Release Status"),
            values=[_(u'Quarintened'), _(u'Released'), _(u'Consumed')],
            required=True,
    )
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
    PBS10xBatch = schema.Int(
            title=_(u"Batch Number"),
            description=_(u"Batch number of solution"),
            required=True,
            )
    PBS10xTotalVolume = schema.Choice(
            title=_(u"Solution Volume"),
            description=_(u"Volume of solution"),
            values =[_(u"5L"),\
                   _(u"2.5L")], 
            required=True,
            )
    PBS10xMakeDate = schema.Date(
            title=_(u"Date Made"),
            description=_(u"Data Solution was Made"),
            required=True,
            )
    PBS10xExpDate = schema.Date(
            title=_(u"Expiration Date"),
            description=_(u"Expiration Date"),
            required=True,
            )
    PBS10xViability = schema.Int(
            title=_(u"Solution Viability"),
            description=_(u"Viability of solution in hours"),
            required=False,
            )
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
    OnePercentCaseinBatch = schema.Int(
            title=_(u"Batch Number"),
            description=_(u"Batch number of solution"),
            required=True,
            )
    OnePercentCaseinMadeDate = schema.Date(
            title=_(u"Date Made"),
            description=_(u"Data Solution was Made"),
            required=True,
            )
    OnePercentCaseinExpirationDate = schema.Date(
            title=_(u"Expiration Date"),
            description=_(u"Expiration Date"),
            #value = 
            required=True,
            )
    OnePercentCaseinVolume = schema.Choice(
            title=_(u"Solution Volume"),
            description=_(u"Volume of solution"),
            values =[_(u"50 mL"),\
                   _(u"25 mL")], 
            required=True,
            )
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
    OnePercentCaseinViability = schema.Int(
            title=_(u"Solution Viability"),
            description=_(u"Viability of solution in hours"),
            required=False,
            )
class ITween22_4Percentinpbs(model.Schema):
    Tween22Batch = schema.Int(
            title=_(u"Batch Number"),
            description=_(u"Batch number of solution"),
            required=True,
            )
    Tween22ExpDate = schema.Date(
            title=_(u"Expiration Date"),
            description=_(u"Expiration Date"),
            required=True,
            )
    Tween22MakeDate = schema.Date(
            title=_(u"Date Made"),
            description=_(u"Data Solution was Made"),
            required=True,
            )
    Tween22Viability = schema.Int(
            title=_(u"Solution Viability"),
            description=_(u"Viability of solution in hours"),
            required=False,
            )
    Tween22Volume = schema.Float(
            title=_(u"Solution Volume"),
            description=_(u"Volume of solution"),
            required=False,
            )
class I1mgpermlIgg_cy3(model.Schema):
    OnemgpermlIgg_cy3Batch = schema.Int(
            title=_(u"Batch Number"),
            description=_(u"Batch number of solution"),
            required=True,
            )
    OnemgpermlIgg_cy3ExpDate = schema.Date(
            title=_(u"Expiration Date"),
            description=_(u"Expiration Date"),
            required=True,
            )
    OnemgpermlIgg_cy3MakeDate = schema.Date(
            title=_(u"Date Made"),
            description=_(u"Data Solution was Made"),
            required=True,
            )
    OnemgpermlIgg_cy3Viability = schema.Int(
            title=_(u"Solution Viability"),
            description=_(u"Viability of solution in hours"),
            required=False,
            )
    OnemgpermlIgg_cy3Volume = schema.Float(
            title=_(u"Solution Volume"),
            description=_(u"Volume of solution"),
            required=False,
            )
class I1mgpermlIgm_af647(model.Schema):
    OnemgpermlIgm_af647Batch = schema.Int(
            title=_(u"Batch Number"),
            description=_(u"Batch number of solution"),
            required=True,
            )
    OnemgpermlIgm_af647ExpDate = schema.Date(
            title=_(u"Expiration Date"),
            description=_(u"Expiration Date"),
            required=True,
            )
    OnemgpermlIgm_af647MakeDate = schema.Date(
            title=_(u"Date Made"),
            description=_(u"Data Solution was Made"),
            required=True,
            )
    OnemgpermlIgm_af647Viability = schema.Int(
            title=_(u"Solution Viability"),
            description=_(u"Viability of solution in hours"),
            required=False,
            )
    OnemgpermlIgm_af647Volume = schema.Float(
            title=_(u"Solution Volume"),
            description=_(u"Volume of solution"),
            required=False,
            )
class I3Mkcl(model.Schema):
    ThreeMkclBatch = schema.Int(
            title=_(u"Batch Number"),
            description=_(u"Batch number of solution"),
            required=True,
            )
    ThreeMkclExpDate = schema.Date(
            title=_(u"Expiration Date"),
            description=_(u"Expiration Date"),
            required=True,
            )
    ThreeMkclMakeDate = schema.Date(
            title=_(u"Date Made"),
            description=_(u"Data Solution was Made"),
            required=True,
            )
    ThreeMkclViability = schema.Int(
            title=_(u"Solution Viability"),
            description=_(u"Viability of solution in hours"),
            required=False,
            )
    ThreeMkclVolume = schema.Float(
            title=_(u"Solution Volume"),
            description=_(u"Volume of solution"),
            required=False,
            )
class I50PercentGlycerol(model.Schema):
    FiftyPercentGlycerolBatch = schema.Int(
            title=_(u"Batch Number"),
            description=_(u"Batch number of solution"),
            required=True,
            )
    FiftyPercentGlycerolExpDate = schema.Date(
            title=_(u"Expiration Date"),
            description=_(u"Expiration Date"),
            required=True,
            )
    FiftyPercentGlycerolMakeDate = schema.Date(
            title=_(u"Date Made"),
            description=_(u"Data Solution was Made"),
            required=True,
            )
    FiftyPercentGlycerolViability = schema.Int(
            title=_(u"Solution Viability"),
            description=_(u"Viability of solution in hours"),
            required=False,
            )
    FiftyPercentGlycerolVolume = schema.Float(
            title=_(u"Solution Volume"),
            description=_(u"Volume of solution"),
            required=False,
            )
class I70PercentEthyanol(model.Schema):
    SeventyPercentEthyanolBatch = schema.Int(
            title=_(u"Batch Number"),
            description=_(u"Batch number of solution"),
            required=True,
            )
    SeventyPercentEthyanolExpDate = schema.Date(
            title=_(u"Expiration Date"),
            description=_(u"Expiration Date"),
            required=True,
            )
    SeventyPercentEthyanolMakeDate = schema.Date(
            title=_(u"Date Made"),
            description=_(u"Data Solution was Made"),
            required=True,
            )
    SeventyPercentEthyanolViability = schema.Int(
            title=_(u"Solution Viability"),
            description=_(u"Viability of solution in hours"),
            required=False,
            )
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
class I10Percenthcl(model.Schema):
    TenPercenthclBatch = schema.Int(
            title=_(u"Batch Number"),
            description=_(u"Batch number of solution"),
            required=True,
            )
    TenPercenthclExpDate = schema.Date(
            title=_(u"Expiration Date"),
            description=_(u"Expiration Date"),
            required=True,
            )
    TenPercenthclMakeDate = schema.Date(
            title=_(u"Date Made"),
            description=_(u"Data Solution was Made"),
            required=True,
            )
    TenPercenthclViability = schema.Int(
            title=_(u"Solution Viability"),
            description=_(u"Viability of solution in hours"),
            required=False,
            )
    TenPercenthclVolume = schema.Float(
            title=_(u"Solution Volume"),
            description=_(u"Volume of solution"),
            required=False,
            )

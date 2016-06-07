"""To add custome slide content to immunarray.lims
"""
import datetime

from zope import schema
from zope.interface import implements

from immunarray.lims import _
from plone.namedfile import field as namedfile
from plone.supermodel import model
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


# XXX IMateral for base fields

class ICaseinSalt(model.Schema):
    CaseinSaltLot = schema.ASCIILine(
        title=_(u"Casein Salt Lot"),
        description=_(u"Lot of Casein Salt"),
        required=True,
    )
    CaseinSaltVendor = schema.ASCIILine(
        title=_(u"Casein Salt Vendor"),
        description=_(u"Vendor of Casein Salt"),
        required=True,
    )
    CaseinSaltCatalogNumber = schema.ASCIILine(
        title=_(u"Casein Salt Catalog Number"),
        description=_(u"Catalog Number of Casein Salt"),
        required=True,
    )
    CaseinSaltArrivalDate = schema.Date(
        title=_(u"Arrival Data of Casein Salt"),
        description=_(u"Arrival Date of Casein Salt"),
        required=True,
    )
    CaseinSaltExpDate = schema.Date(
        title=_(u"Expiration Date"),
        description=_(u"Expiration Date"),
        required=True,
    )
    CaseinSaltCofA = namedfile.NamedBlobImage(
        title=_(u"Certificate of Analysis"),
        description=_(u"Certificate of Analysis"),
        required=True,
    )
    CaseinSaltStatus = schema.Choice(
        title=_(u"Status"),
        description=_(u"Casein Salt Release Status"),
        values=[_(u'Quarintened'), _(u'Released'), _(u'Consumed')],
        required=True,
    )
    CaseinSaltArrivalMass = schema.Int(
        title=_(u"Arrival Mass of Casein Salt"),
        description=_(u"Mass of Casein Salt on Arrival"),
        required=False,
    )
    CaseinSaltCurrentMass = schema.Int(
        title=_(u"Current Mass of Casein Salt"),
        description=_(u"Current Mass of Casein Salt"),
        required=False,
    )
    CaseinSaltReciviedBy = schema.Choice(
        title=_(u"Operator that Recivied Casein Salt"),
        description=_(u"Operator that recivied material"),
        vocabulary=u"plone.principalsource.Users",
        required=True,
    )
    CaseinSaltOpenedBy = schema.Choice(
        title=_(u"Operator that Opened Casein Salt"),
        description=_(u"Operator that Opened Casein Salt"),
        vocabulary=u"plone.principalsource.Users",
        required=False,
    )


class ISodiumChloride(model.Schema):
    SodiumChlorideLot = schema.ASCIILine(
        title=_(u"Sodium Chloride Lot"),
        description=_(u"Lot of Sodium Chloride"),
        required=True,
    )
    SodiumChlorideVendor = schema.ASCIILine(
        title=_(u"Vendor"),
        description=_(u"Vendor of Sodium Chloride"),
        required=True,
    )
    SodiumChlorideCatalogNumber = schema.ASCIILine(
        title=_(u"Sodium Chloride Catalog #"),
        description=_(u"Catalog # of Sodium Chloride"),
        required=True,
    )
    SodiumChlorideExpDate = schema.Date(
        title=_(u"Expiration Date"),
        description=_(u"Expiration Date"),
        required=True,
    )
    SodiumChlorideArrivalDate = schema.Date(
        title=_(u"Arrival Data of Sodium Chloride"),
        description=_(u"Arrival Date of Sodium Chloride"),
        required=True,
    )
    SodiumChlorideCofA = namedfile.NamedBlobImage(
        title=_(u"Certificate of Analysis"),
        description=_(u"Certificate of Analysis"),
        required=True,
    )
    SodiumChlorideStatus = schema.Choice(
        title=_(u"Status"),
        description=_(u"Sodium Chloride Release Status"),
        values=[_(u'Quarintened'), _(u'Released'), _(u'Consumed')],
        required=True,
    )
    SodiumChlorideArrivalMass = schema.Int(
        title=_(u"Arrival Mass of Sodium Chloride"),
        description=_(u"Mass of Sodium Chloride on Arrival"),
        required=False,
    )
    SodiumChlorideCurrentMass = schema.Int(
        title=_(u"Current Mass of Sodium Chloride"),
        description=_(u"Current Mass of Sodium Chloride"),
        required=False,
    )
    SodiumChlorideReciviedBy = schema.Choice(
        title=_(u"Operator that Recivied Sodium Chloride"),
        description=_(u"Operator that recivied Sodium Chloride"),
        vocabulary=u"plone.principalsource.Users",
        required=True,
    )
    SodiumChlorideOpenedBy = schema.Choice(
        title=_(u"Operator that Opened Sodium Chloride"),
        description=_(u"Operator that opened Sodium Chloride"),
        vocabulary=u"plone.principalsource.Users",
        required=False,
    )


class IPotassiumChloride(model.Schema):
    PotassiumChlorideLot = schema.ASCIILine(
        title=_(u"Potassium Chloride Lot"),
        description=_(u"Lot of Potassium Chloride"),
        required=True,
    )
    PotassiumChlorideVendor = schema.ASCIILine(
        title=_(u"Potassium Chloride Vendor"),
        description=_(u"Vendor of Potassium Chloride"),
        required=True,
    )
    PotassiumChlorideCatalogNumber = schema.ASCIILine(
        title=_(u"Potassium Chloride Catalog Number"),
        description=_(u"Catalog Number of Potassium Chloride"),
        required=True,
    )
    PotassiumChlorideExpDate = schema.Date(
        title=_(u"Expiration Date"),
        description=_(u"Expiration Date"),
        required=True,
    )
    PotassiumChlorideArrivalDate = schema.Date(
        title=_(u"Arrival Data of Potassium Chloride"),
        description=_(u"Arrival Date of Potassium Chloride"),
        required=True,
    )
    PotassiumChlorideCofA = namedfile.NamedBlobImage(
        title=_(u"Certificate of Analysis"),
        description=_(u"Certificate of Analysis"),
        required=True,
    )
    PotassiumChlorideStatus = schema.Choice(
        title=_(u"Status"),
        description=_(u"Potassium Chloride Release Status"),
        values=[_(u'Quarintened'), _(u'Released'), _(u'Consumed')],
        required=True,
    )
    PotassiumChlorideArrivalMass = schema.Int(
        title=_(u"Arrival Mass of Potassium Chloride"),
        description=_(u"Mass of Potassium Chloride on Arrival"),
        required=False,
    )
    PotassiumChlorideCurrentMass = schema.Int(
        title=_(u"Current Mass of Potassium Chloride"),
        description=_(u"Current Mass of Potassium Chloride"),
        required=False,
    )
    PotassiumChlorideReciviedBy = schema.Choice(
        title=_(u"Operator that Recivied Potassium Chloride"),
        description=_(u"Operator that recivied Potassium Chloride"),
        vocabulary=u"plone.principalsource.Users",
        required=True,
    )
    PotassiumChlorideOpenedBy = schema.Choice(
        title=_(u"Operator that Opened Potassium Chloride"),
        description=_(u"Operator that Opened Potassium Chloride"),
        vocabulary=u"plone.principalsource.Users",
        required=False,
    )


class ISodiumPhosphatedibasic(model.Schema):
    SodiumPhosphatedibasicLot = schema.ASCIILine(
        title=_(u"Sodium Phosphatedibasic Lot"),
        description=_(u"Lot of Solution"),
        required=True,
    )
    SodiumPhosphatedibasicVendor = schema.ASCIILine(
        title=_(u"Sodium Phosphatedibasic Vendor"),
        description=_(u"Vendor of Solution"),
        required=True,
    )
    SodiumPhosphatedibasicCatalogNumber = schema.ASCIILine(
        title=_(u"Sodium Phosphatedibasic Catalog Number"),
        description=_(u"Catalog Number of Solution"),
        required=True,
    )
    SodiumPhosphatedibasicExpDate = schema.Date(
        title=_(u"Expiration Date"),
        description=_(u"Expiration Date"),
        required=True,
    )
    SodiumPhosphatedibasicArrivalDate = schema.Date(
        title=_(u"Arrival Data of Sodium Phosphatedibasic"),
        description=_(u"Arrival Date of Sodium Phosphatedibasic"),
        required=True,
    )
    SodiumPhosphatedibasicCofA = namedfile.NamedBlobImage(
        title=_(u"Certificate of Analysis"),
        description=_(u"Certificate of Analysis"),
        required=True,
    )
    SodiumPhosphatedibasicStatus = schema.Choice(
        title=_(u"Status"),
        description=_(u"Sodium Phosphatedibasic Release Status"),
        values=[_(u'Quarintened'), _(u'Released'), _(u'Consumed')],
        required=True,
    )
    SodiumPhosphatedibasicArrivalMass = schema.Int(
        title=_(u"Arrival Mass of Sodium Phosphatedibasic"),
        description=_(u"Mass of Sodium Phosphatedibasic on Arrival"),
        required=False,
    )
    SodiumPhosphatedibasicCurrentMass = schema.Int(
        title=_(u"Current Mass of Sodium Phosphatedibasic"),
        description=_(u"Current Mass of Sodium Phosphatedibasic"),
        required=False,
    )
    SodiumPhosphatedibasicReciviedBy = schema.Choice(
        title=_(u"Operator that Recivied Sodium Phosphatedibasic"),
        description=_(u"Operator that recivied Sodium Phosphatedibasic"),
        vocabulary=u"plone.principalsource.Users",
        required=True,
    )
    SodiumPhosphatedibasicOpenedBy = schema.Choice(
        title=_(u"Operator that Opened Sodium Phosphatedibasic"),
        description=_(u"Operator that Opened Sodium Phosphatedibasic"),
        vocabulary=u"plone.principalsource.Users",
        required=False,
    )


class IPotassiumPhosphatemonobasic(model.Schema):
    PotassiumPhosphatemonobasicLot = schema.ASCIILine(
        title=_(u"Potassium Phosphatemonobasic Lot"),
        description=_(u"Lot of Potassium Phosphatemonobasic"),
        required=True,
    )
    PotassiumPhosphatemonobasicVendor = schema.ASCIILine(
        title=_(u"Potassium Phosphatemonobasic Vendor"),
        description=_(u"Vendor of Potassium Phosphatemonobasic"),
        required=True,
    )
    PotassiumPhosphatemonobasicCatalogNumber = schema.ASCIILine(
        title=_(u"Potassium Phosphatemonobasic Catalog Number"),
        description=_(u"Catalog Number of Potassium Phosphatemonobasic"),
        required=True,
    )
    PotassiumPhosphatemonobasicExpDate = schema.Date(
        title=_(u"Expiration Date"),
        description=_(u"Expiration Date"),
        required=True,
    )
    PotassiumPhosphatemonobasicArrivalDate = schema.Date(
        title=_(u"Arrival Data of Potassium Phosphatemonobasic"),
        description=_(u"Arrival Date of Potassium Phosphatemonobasic"),
        required=True,
    )
    PotassiumPhosphatemonobasicCofA = namedfile.NamedBlobImage(
        title=_(u"Certificate of Analysis"),
        description=_(u"Certificate of Analysis"),
        required=True,
    )
    PotassiumPhosphatemonobasicStatus = schema.Choice(
        title=_(u"Status"),
        description=_(u"Potassium Phosphatemonobasic Release Status"),
        values=[_(u'Quarintened'), _(u'Released'), _(u'Consumed')],
        required=True,
    )
    PotassiumPhosphatemonobasicArrivalMass = schema.Int(
        title=_(u"Arrival Mass of Potassium Phosphatemonobasic"),
        description=_(u"Mass of Potassium Phosphatemonobasic on Arrival"),
        required=False,
    )
    PotassiumPhosphatemonobasicCurrentMass = schema.Int(
        title=_(u"Current Mass of Potassium Phosphatemonobasic"),
        description=_(u"Current Mass of Potassium Phosphatemonobasic"),
        required=False,
    )
    PotassiumPhosphatemonobasicReciviedBy = schema.Choice(
        title=_(u"Operator that Recivied Potassium Phosphatemonobasic"),
        description=_(u"Operator that recivied Potassium Phosphatemonobasic"),
        vocabulary=u"plone.principalsource.Users",
        required=True,
    )
    PotassiumPhosphatemonobasicOpenedBy = schema.Choice(
        title=_(u"Operator that Opened Potassium Phosphatemonobasic"),
        description=_(u"Operator that Opened Potassium Phosphatemonobasic"),
        vocabulary=u"plone.principalsource.Users",
        required=False,
    )


class ISodiumHydroxide2_5N(model.Schema):
    SodiumHydroxide2_5NLot = schema.ASCIILine(
        title=_(u"Sodium Hydroxide 2.5N Lot"),
        description=_(u"Lot of Sodium Hydroxide 2.5N"),
        required=True,
    )
    SodiumHydroxide2_5NVendor = schema.ASCIILine(
        title=_(u"Sodium Hydroxide 2.5N Vendor"),
        description=_(u"Vendor of Sodium Hydroxide 2.5N"),
        required=True,
    )
    SodiumHydroxide2_5NCatalogNumber = schema.ASCIILine(
        title=_(u"Sodium Hydroxide 2.5N Catalog Number"),
        description=_(u"Catalog Number of Sodium Hydroxide 2.5N"),
        required=True,
    )
    SodiumHydroxide2_5NExpDate = schema.Date(
        title=_(u"Expiration Date"),
        description=_(u"Expiration Date"),
        required=True,
    )
    SodiumHydroxide2_5NArrivalDate = schema.Date(
        title=_(u"Arrival Data of Sodium Hydroxide 2.5N"),
        description=_(u"Arrival Date of Sodium Hydroxide 2.5N"),
        required=True,
    )
    SodiumHydroxide2_5NCofA = namedfile.NamedBlobImage(
        title=_(u"Certificate of Analysis"),
        description=_(u"Certificate of Analysis"),
        required=True,
    )
    SodiumHydroxide2_5NStatus = schema.Choice(
        title=_(u"Status"),
        description=_(u"Sodium Hydroxide 2.5N Release Status"),
        values=[_(u'Quarintened'), _(u'Released'), _(u'Consumed')],
        required=True,
    )
    SodiumHydroxide2_5NArrivalVolume = schema.Int(
        title=_(u"Arrival Volume of Sodium Hydroxide 2.5N"),
        description=_(u"Arrival Volume of Sodium Hydroxide 2.5N"),
        required=False,
    )
    SodiumHydroxide2_5NCurrentVolume = schema.Int(
        title=_(u"Current Volume of Sodium Hydroxide 2.5N"),
        description=_(u"Current Volume of Sodium Hydroxide 2.5N"),
        required=False,
    )
    SodiumHydroxide2_5NReciviedBy = schema.Choice(
        title=_(u"Operator that Recivied Sodium Hydroxide 2.5N"),
        description=_(u"Operator that recivied Sodium Hydroxide 2.5N"),
        vocabulary=u"plone.principalsource.Users",
        required=True,
    )
    SodiumHydroxide2_5NOpenedBy = schema.Choice(
        title=_(u"Operator that Opened Sodium Hydroxide 2.5N"),
        description=_(u"Operator that Opened Sodium Hydroxide 2.5N"),
        vocabulary=u"plone.principalsource.Users",
        required=False,
    )


class IEthylalcholDenaturedReagentGrade(model.Schema):
    EthylalcholDenaturedReagentGradeLot = schema.ASCIILine(
        title=_(u"Ethylalchol (Denatured Reagent Grade) Lot"),
        description=_(u"Lot of Ethylalchol (Denatured Reagent Grade)"),
        required=True,
    )
    EthylalcholDenaturedReagentGradeVendor = schema.ASCIILine(
        title=_(u"Ethylalchol (Denatured Reagent Grade) Vendor"),
        description=_(u"Vendor of Ethylalchol (Denatured Reagent Grade)"),
        required=True,
    )
    EthylalcholDenaturedReagentGradeCatalogNumber = schema.ASCIILine(
        title=_(u"Ethylalchol (Denatured Reagent Grade) Catalog Number"),
        description=_(
            u"Catalog Number of Ethylalchol (Denatured Reagent Grade)"),
        required=True,
    )
    EthylalcholDenaturedReagentGradeExpDate = schema.Date(
        title=_(u"Expiration Date"),
        description=_(u"Expiration Date"),
        required=True,
    )
    EthylalcholDenaturedReagentGradeArrivalDate = schema.Date(
        title=_(u"Arrival Data of Ethylalchol (Denatured Reagent Grade)"),
        description=_(u"Arrival Date of Ethylalchol (Denatured Reagent Grade)"),
        required=True,
    )
    EthylalcholDenaturedReagentGradeCofA = namedfile.NamedBlobImage(
        title=_(u"Certificate of Analysis"),
        description=_(u"Certificate of Analysis"),
        required=True,
    )
    EthylalcholDenaturedReagentGradeStatus = schema.Choice(
        title=_(u"Status"),
        description=_(u"Ethylalchol (Denatured Reagent Grade) Release Status"),
        values=[_(u'Quarintened'), _(u'Released'), _(u'Consumed')],
        required=True,
    )
    EthylalcholDenaturedReagentGradeArrivalVolume = schema.Int(
        title=_(u"Arrival Volume of Ethylalchol (Denatured Reagent Grade)"),
        description=_(
            u"Arrival Volume of Ethylalchol (Denatured Reagent Grade)"),
        required=False,
    )
    EthylalcholDenaturedReagentGradeCurrentVolume = schema.Int(
        title=_(u"Current Volume of Ethylalchol (Denatured Reagent Grade)"),
        description=_(
            u"Current Volume of Ethylalchol (Denatured Reagent Grade)"),
        required=False,
    )
    EthylalcholDenaturedReagentGradeReciviedBy = schema.Choice(
        title=_(
            u"Operator that Recivied Ethylalchol (Denatured Reagent Grade)"),
        description=_(
            u"Operator that recivied Ethylalchol (Denatured Reagent Grade)"),
        vocabulary=u"plone.principalsource.Users",
        required=True,
    )
    EthylalcholDenaturedReagentGradeOpenedBy = schema.Choice(
        title=_(u"Operator that Opened Ethylalchol (Denatured Reagent Grade)"),
        description=_(
            u"Operator that Opened Ethylalchol (Denatured Reagent Grade)"),
        vocabulary=u"plone.principalsource.Users",
        required=False,
    )


class ITween20(model.Schema):
    Tween20Lot = schema.ASCIILine(
        title=_(u"Tween 20 Lot"),
        description=_(u"Lot of Solution"),
        required=True,
    )
    Tween20Vendor = schema.ASCIILine(
        title=_(u"Tween 20 Vendor"),
        description=_(u"Vendor of Solution"),
        required=True,
    )
    Tween20CatalogNumber = schema.ASCIILine(
        title=_(u"Tween 20 Catalog Number"),
        description=_(u"Catalog Number of Solution"),
        required=True,
    )
    Tween20ExpDate = schema.Date(
        title=_(u"Expiration Date"),
        description=_(u"Expiration Date"),
        required=True,
    )
    Tween20ArrivalDate = schema.Date(
        title=_(u"Arrival Data of Tween 20"),
        description=_(u"Arrival Date of Tween 20"),
        required=True,
    )
    Tween20CofA = namedfile.NamedBlobImage(
        title=_(u"Certificate of Analysis"),
        description=_(u"Certificate of Analysis"),
        required=True,
    )
    Tween20Status = schema.Choice(
        title=_(u"Status"),
        description=_(u"Tween 20 Release Status"),
        values=[_(u'Quarintened'), _(u'Released'), _(u'Consumed')],
        required=True,
    )
    Tween20ArrivalMass = schema.Int(
        title=_(u"Arrival Mass of Tween 20"),
        description=_(u"Mass of Tween 20 on Arrival"),
        required=False,
    )
    Tween20CurrentMass = schema.Int(
        title=_(u"Current Mass of Tween 20"),
        description=_(u"Current Mass of Tween 20"),
        required=False,
    )
    Tween20ReciviedBy = schema.Choice(
        title=_(u"Operator that Recivied Tween 20"),
        description=_(u"Operator that recivied Tween 20"),
        vocabulary=u"plone.principalsource.Users",
        required=True,
    )
    Tween20OpenedBy = schema.Choice(
        title=_(u"Operator that Opened Tween 20"),
        description=_(u"Operator that Opened Tween 20"),
        vocabulary=u"plone.principalsource.Users",
        required=False,
    )


class IHydrochloricacid37Percent(model.Schema):
    Hydrochloricacid37PercentLot = schema.ASCIILine(
        title=_(u"Hydrochloricacid 37% Lot"),
        description=_(u"Lot of Hydrochloricacid 37%"),
        required=True,
    )
    Hydrochloricacid37PercentVendor = schema.ASCIILine(
        title=_(u"Hydrochloricacid 37% Vendor"),
        description=_(u"Vendor of Hydrochloricacid 37%"),
        required=True,
    )
    Hydrochloricacid37PercentCatalogNumber = schema.ASCIILine(
        title=_(u"Hydrochloricacid 37% Catalog Number"),
        description=_(u"Catalog Number of Hydrochloricacid 37%"),
        required=True,
    )
    Hydrochloricacid37PercentExpDate = schema.Date(
        title=_(u"Expiration Date"),
        description=_(u"Expiration Date"),
        required=True,
    )
    Hydrochloricacid37PercentArrivalDate = schema.Date(
        title=_(u"Arrival Data of Hydrochloricacid 37%"),
        description=_(u"Arrival Date of Hydrochloricacid 37%"),
        required=True,
    )
    Hydrochloricacid37PercentCofA = namedfile.NamedBlobImage(
        title=_(u"Certificate of Analysis"),
        description=_(u"Certificate of Analysis"),
        required=True,
    )
    Hydrochloricacid37PercentStatus = schema.Choice(
        title=_(u"Status"),
        description=_(u"Hydrochloricacid 37% Release Status"),
        values=[_(u'Quarintened'), _(u'Released'), _(u'Consumed')],
        required=True,
    )
    Hydrochloricacid37PercentArrivalVolume = schema.Int(
        title=_(u"Arrival Volume of Hydrochloricacid 37%"),
        description=_(u"Arrival Volume of Hydrochloricacid 37%"),
        required=False,
    )
    Hydrochloricacid37PercentCurrentVolume = schema.Int(
        title=_(u"Current Volume of Hydrochloricacid 37%"),
        description=_(u"Current Volume of Hydrochloricacid 37%"),
        required=False,
    )
    Hydrochloricacid37PercentReciviedBy = schema.Choice(
        title=_(u"Operator that Recivied Hydrochloricacid 37%"),
        description=_(u"Operator that recivied Hydrochloricacid 37%"),
        vocabulary=u"plone.principalsource.Users",
        required=True,
    )
    Hydrochloricacid37PercentOpenedBy = schema.Choice(
        title=_(u"Operator that Opened Hydrochloricacid 37%"),
        description=_(u"Operator that Opened Hydrochloricacid 37%"),
        vocabulary=u"plone.principalsource.Users",
        required=False,
    )


class IGlycerol(model.Schema):
    GlycerolLot = schema.ASCIILine(
        title=_(u"Glycerol Lot"),
        description=_(u"Lot of Hydrochloricacid 37%"),
        required=True,
    )
    GlycerolVendor = schema.ASCIILine(
        title=_(u"Glycerol Vendor"),
        description=_(u"Vendor of Hydrochloricacid 37%"),
        required=True,
    )
    GlycerolCatalogNumber = schema.ASCIILine(
        title=_(u"Glycerol Catalog Number"),
        description=_(u"Catalog Number of Hydrochloricacid 37%"),
        required=True,
    )
    GlycerolExpDate = schema.Date(
        title=_(u"Expiration Date"),
        description=_(u"Expiration Date"),
        required=True,
    )
    GlycerolArrivalDate = schema.Date(
        title=_(u"Arrival Data of Glycerol"),
        description=_(u"Arrival Date of Glycerol"),
        required=True,
    )
    GlycerolCofA = namedfile.NamedBlobImage(
        title=_(u"Certificate of Analysis"),
        description=_(u"Certificate of Analysis"),
        required=True,
    )
    GlycerolStatus = schema.Choice(
        title=_(u"Status"),
        description=_(u"Glycerol Release Status"),
        values=[_(u'Quarintened'), _(u'Released'), _(u'Consumed')],
        required=True,
    )
    GlycerolArrivalVolume = schema.Int(
        title=_(u"Arrival Volume of Glycerol"),
        description=_(u"Arrival Volume of Glycerol"),
        required=False,
    )
    GlycerolCurrentVolume = schema.Int(
        title=_(u"Current Volume of Glycerol"),
        description=_(u"Current Volume of Glycerol"),
        required=False,
    )
    GlycerolReciviedBy = schema.Choice(
        title=_(u"Operator that Recivied Glycerol"),
        description=_(u"Operator that recivied Glycerol"),
        vocabulary=u"plone.principalsource.Users",
        required=True,
    )
    GlycerolOpenedBy = schema.Choice(
        title=_(u"Operator that Opened Glycerol"),
        description=_(u"Operator that Opened Glycerol"),
        vocabulary=u"plone.principalsource.Users",
        required=False,
    )


class IIgg_Cy3(model.Schema):
    Igg_Cy3Lot = schema.ASCIILine(
        title=_(u"IgG-Cy3 Lot"),
        description=_(u"Lot of IgG-Cy3"),
        required=True,
    )
    Igg_Cy3Vendor = schema.ASCIILine(
        title=_(u"IgG-Cy3 Vendor"),
        description=_(u"Vendor of IgG-Cy3"),
        required=True,
    )
    Igg_Cy3CatalogNumber = schema.ASCIILine(
        title=_(u"IgG-Cy3 Catalog Number"),
        description=_(u"Catalog Number of IgG-Cy3"),
        required=True,
    )
    Igg_Cy3ExpDate = schema.Date(
        title=_(u"Expiration Date"),
        description=_(u"Expiration Date"),
        required=True,
    )
    Igg_Cy3ArrivalDate = schema.Date(
        title=_(u"Arrival Data of IgG-Cy3"),
        description=_(u"Arrival Date of IgG-Cy3"),
        required=True,
    )
    Igg_Cy3CofA = namedfile.NamedBlobImage(
        title=_(u"Certificate of Analysis"),
        description=_(u"Certificate of Analysis"),
        required=True,
    )
    Igg_Cy3Status = schema.Choice(
        title=_(u"Status"),
        description=_(u"IgG-Cy3 Release Status"),
        values=[_(u'Quarintened'), _(u'Released'), _(u'Consumed')],
        required=True,
    )
    Igg_Cy3ArrivalMass = schema.Int(
        title=_(u"Arrival Mass of IgG-Cy3"),
        description=_(u"Mass of IgG-Cy3 on Arrival"),
        required=False,
    )
    Igg_Cy3CurrentMass = schema.Int(
        title=_(u"Current Mass of IgG-Cy3"),
        description=_(u"Current Mass of IgG-Cy3"),
        required=False,
    )
    Igg_Cy3ReciviedBy = schema.Choice(
        title=_(u"Operator that Recivied IgG-Cy3"),
        description=_(u"Operator that recivied IgG-Cy3"),
        vocabulary=u"plone.principalsource.Users",
        required=True,
    )
    Igg_Cy3OpenedBy = schema.Choice(
        title=_(u"Operator that Opened IgG-Cy3"),
        description=_(u"Operator that Opened IgG-Cy3"),
        vocabulary=u"plone.principalsource.Users",
        required=False,
    )


class IIgm_Af647(model.Schema):
    Igm_Af647Lot = schema.ASCIILine(
        title=_(u"IgM-Af647 Lot"),
        description=_(u"Lot of IgM-Af647"),
        required=True,
    )
    Igm_Af647Vendor = schema.ASCIILine(
        title=_(u"IgM-Af647 Vendor"),
        description=_(u"Vendor of IgM-Af647"),
        required=True,
    )
    Igm_Af647CatalogNumber = schema.ASCIILine(
        title=_(u"IgM-Af647 Catalog Number"),
        description=_(u"Catalog Number of IgM-Af647"),
        required=True,
    )
    Igm_Af647ExpDate = schema.Date(
        title=_(u"Expiration Date"),
        description=_(u"Expiration Date"),
        required=True,
    )
    Igm_Af647ArrivalDate = schema.Date(
        title=_(u"Arrival Data of IgM-Af647"),
        description=_(u"Arrival Date of IgM-Af647"),
        required=True,
    )
    Igm_Af647CofA = namedfile.NamedBlobImage(
        title=_(u"Certificate of Analysis"),
        description=_(u"Certificate of Analysis"),
        required=True,
    )
    Igm_Af647Status = schema.Choice(
        title=_(u"Status"),
        description=_(u"IgM-Af647 Release Status"),
        values=[_(u'Quarintened'), _(u'Released'), _(u'Consumed')],
        required=True,
    )
    Igm_Af647ArrivalMass = schema.Int(
        title=_(u"Arrival Mass of IgM-Af647"),
        description=_(u"Mass of IgM-Af647 on Arrival"),
        required=False,
    )
    Igm_Af647CurrentMass = schema.Int(
        title=_(u"Current Mass of IgM-Af647"),
        description=_(u"Current Mass of IgM-Af647"),
        required=False,
    )
    Igm_Af647ReciviedBy = schema.Choice(
        title=_(u"Operator that Recivied IgM-Af647"),
        description=_(u"Operator that recivied IgM-Af647"),
        vocabulary=u"plone.principalsource.Users",
        required=True,
    )
    Igm_Af647OpenedBy = schema.Choice(
        title=_(u"Operator that Opened IgM-Af647"),
        description=_(u"Operator that Opened IgM-Af647"),
        vocabulary=u"plone.principalsource.Users",
        required=False,
    )


# Solution vocabs
class PBS10xlotVocabulary(object):
    """Vocabulary factory to pull single unfiltered data element
    Call by using (vocabulary="immunarray.lims.content.vocabulary.PBS10xlotVocabulary")
    """
    implements(IVocabularyFactory)

    def __call__(self, context):
        translate = context.translate
        catalog = context.portal_catalog
        proxies = catalog(
            object_provides="immunarray.lims.content.solution.I10xpbs")
        vocabularydata = []
        items = []
        for proxy in proxies:
            solution = proxy.getObject()
            if solution.PBS10xExpDate >= datetime.datetime.now().date():
                vocabularydata.append(solution.PBS10xBatch)
            items = [SimpleTerm(i) for i in vocabularydata]
        return SimpleVocabulary(items)


PBS10xlotVocabularyFactory = PBS10xlotVocabulary()


class PBS1xlotVocabulary(object):
    """Vocabulary factory to pull single unfiltered data element
    Call by using (vocabulary="immunarray.lims.content.solution.PBS1xlotVocabulary")
    """
    implements(IVocabularyFactory)

    def __call__(self, context):
        translate = context.translate
        catalog = context.portal_catalog
        proxies = catalog(
            object_provides="immunarray.lims.content.solution.I1xpbs")
        vocabularydata = []
        items = []
        for proxy in proxies:
            material = proxy.getObject()
            if material.PBS1xExpDate >= datetime.datetime.now().date():
                vocabularydata.append(material.PBS1xBatch)
            items = [SimpleTerm(i) for i in vocabularydata]
        return SimpleVocabulary(items)


PBS1xlotVocabularyFactory = PBS1xlotVocabulary()


# Material vocabs
class CaseinSaltVocabulary(object):
    """Vocabulary factory to pull single unfiltered data element
    Call by using (vocabulary="immunarray.lims.content.vocabulary.CaseinSaltVocabulary")
    """
    implements(IVocabularyFactory)

    def __call__(self, context):
        translate = context.translate
        catalog = context.portal_catalog
        proxies = catalog(
            object_provides="immunarray.lims.content.material.ICaseinSalt")
        vocabularydata = []
        items = []
        for proxy in proxies:
            material = proxy.getObject()
            if material.CaseinSaltStatus == 'Released' and material.CaseinSaltExpDate >= datetime.datetime.now().date():
                vocabularydata.append(material.CaseinSaltLot)
            items = [SimpleTerm(i) for i in vocabularydata]
        return SimpleVocabulary(items)


CaseinSaltVocabularyFactory = CaseinSaltVocabulary()


class SodiumChlorideVocabulary(object):
    """Vocabulary factory to pull single unfiltered data element
    Call by using (vocabulary="immunarray.lims.content.vocabulary.SodiumChlorideVocabulary")
    """
    implements(IVocabularyFactory)

    def __call__(self, context):
        translate = context.translate
        catalog = context.portal_catalog
        proxies = catalog(
            object_provides="immunarray.lims.content.material.ISodiumChloride")
        vocabularydata = []
        items = []
        for proxy in proxies:
            material = proxy.getObject()
            if material.SodiumChlorideStatus == 'Released' and material.SodiumChlorideExpDate >= datetime.datetime.now().date():
                vocabularydata.append(material.SodiumChlorideLot)
            items = [SimpleTerm(i) for i in vocabularydata]
        return SimpleVocabulary(items)


SodiumChlorideVocabularyFactory = SodiumChlorideVocabulary()


class PotassiumChlorideVocabulary(object):
    """Vocabulary factory to pull single unfiltered data element
    Call by using (vocabulary="immunarray.lims.content.vocabulary.PotassiumChlorideVocabulary")
    """
    implements(IVocabularyFactory)

    def __call__(self, context):
        translate = context.translate
        catalog = context.portal_catalog
        proxies = catalog(
            object_provides="immunarray.lims.content.material.IPotassiumChloride")
        vocabularydata = []
        items = []
        for proxy in proxies:
            material = proxy.getObject()
            if material.PotassiumChlorideStatus == 'Released' and material.PotassiumChlorideExpDate >= datetime.datetime.now().date():
                vocabularydata.append(material.PotassiumChlorideLot)
            items = [SimpleTerm(i) for i in vocabularydata]
        return SimpleVocabulary(items)


PotassiumChlorideVocabularyFactory = PotassiumChlorideVocabulary()


class SodiumPhosphatedibasicVocabulary(object):
    """Vocabulary factory to pull single unfiltered data element
    Call by using (vocabulary="immunarray.lims.content.vocabulary.SodiumPhosphatedibasicVocabulary")
    """
    implements(IVocabularyFactory)

    def __call__(self, context):
        translate = context.translate
        catalog = context.portal_catalog
        proxies = catalog(
            object_provides="immunarray.lims.content.material.ISodiumPhosphatedibasic")
        vocabularydata = []
        items = []
        for proxy in proxies:
            material = proxy.getObject()
            if material.SodiumPhosphatedibasicStatus == 'Released' and material.SodiumPhosphatedibasicExpDate >= datetime.datetime.now().date():
                vocabularydata.append(material.SodiumPhosphatedibasicLot)
            items = [SimpleTerm(i) for i in vocabularydata]
        return SimpleVocabulary(items)


SodiumPhosphatedibasicVocabularyFactory = SodiumPhosphatedibasicVocabulary()


class PotassiumPhosphatemonobasicVocabulary(object):
    """Vocabulary factory to pull single unfiltered data element
    Call by using (vocabulary="immunarray.lims.content.vocabulary.PotassiumPhosphatemonobasicVocabulary")
    """
    implements(IVocabularyFactory)

    def __call__(self, context):
        translate = context.translate
        catalog = context.portal_catalog
        proxies = catalog(
            object_provides="immunarray.lims.content.material.IPotassiumPhosphatemonobasic")
        vocabularydata = []
        items = []
        for proxy in proxies:
            material = proxy.getObject()
            if material.PotassiumPhosphatemonobasicStatus == 'Released' and material.PotassiumPhosphatemonobasicExpDate >= datetime.datetime.now().date():
                vocabularydata.append(material.PotassiumPhosphatemonobasicLot)
            items = [SimpleTerm(i) for i in vocabularydata]
        return SimpleVocabulary(items)


PotassiumPhosphatemonobasicVocabularyFactory = PotassiumPhosphatemonobasicVocabulary()


class SodiumHydroxide2_5NVocabulary(object):
    """Vocabulary factory to pull single unfiltered data element
    Call by using (vocabulary="immunarray.lims.content.vocabulary.SodiumHydroxide2_5NVocabulary")
    """
    implements(IVocabularyFactory)

    def __call__(self, context):
        translate = context.translate
        catalog = context.portal_catalog
        proxies = catalog(
            object_provides="immunarray.lims.content.material.ISodiumHydroxide2_5N")
        vocabularydata = []
        items = []
        for proxy in proxies:
            material = proxy.getObject()
            if material.SodiumHydroxide2_5NStatus == 'Released' and material.SodiumHydroxide2_5NExpDate >= datetime.datetime.now().date():
                vocabularydata.append(material.SodiumHydroxide2_5NLot)
            items = [SimpleTerm(i) for i in vocabularydata]
        return SimpleVocabulary(items)


SodiumHydroxide2_5NVocabularyFactory = SodiumHydroxide2_5NVocabulary()


class EthylalcholDenaturedReagentGradeVocabulary(object):
    """Vocabulary factory to pull single unfiltered data element
    Call by using (vocabulary="immunarray.lims.content.vocabulary.EthylalcholDenaturedReagentGradeVocabulary")
    """
    implements(IVocabularyFactory)

    def __call__(self, context):
        translate = context.translate
        catalog = context.portal_catalog
        proxies = catalog(
            object_provides="immunarray.lims.content.material.IEthylalcholDenaturedReagentGrade")
        vocabularydata = []
        items = []
        for proxy in proxies:
            material = proxy.getObject()
            if material.EthylalcholDenaturedReagentGradeStatus == 'Released' and material.EthylalcholDenaturedReagentGradeExpDate >= datetime.datetime.now().date():
                vocabularydata.append(
                    material.EthylalcholDenaturedReagentGradeLot)
            items = [SimpleTerm(i) for i in vocabularydata]
        return SimpleVocabulary(items)


EthylalcholDenaturedReagentGradeVocabularyFactory = EthylalcholDenaturedReagentGradeVocabulary()


class Tween20Vocabulary(object):
    """Vocabulary factory to pull single unfiltered data element
    Call by using (vocabulary="immunarray.lims.content.vocabulary.Tween20Vocabulary")
    """
    implements(IVocabularyFactory)

    def __call__(self, context):
        translate = context.translate
        catalog = context.portal_catalog
        proxies = catalog(
            object_provides="immunarray.lims.content.material.ITween20")
        vocabularydata = []
        items = []
        for proxy in proxies:
            material = proxy.getObject()
            if material.Tween20Status == 'Released' and material.Tween20ExpDate >= datetime.datetime.now().date():
                vocabularydata.append(material.Tween20Lot)
            items = [SimpleTerm(i) for i in vocabularydata]
        return SimpleVocabulary(items)


Tween20VocabularyFactory = Tween20Vocabulary()


class Hydrochloricacid37PercentVocabulary(object):
    """Vocabulary factory to pull single unfiltered data element
    Call by using (vocabulary="immunarray.lims.content.vocabulary.Hydrochloricacid37PercentVocabulary")
    """
    implements(IVocabularyFactory)

    def __call__(self, context):
        translate = context.translate
        catalog = context.portal_catalog
        proxies = catalog(
            object_provides="immunarray.lims.content.material.IHydrochloricacid37Percent")
        vocabularydata = []
        items = []
        for proxy in proxies:
            material = proxy.getObject()
            if material.Hydrochloricacid37PercentStatus == 'Released' and material.Hydrochloricacid37PercentExpDate >= datetime.datetime.now().date():
                vocabularydata.append(material.Hydrochloricacid37PercentLot)
            items = [SimpleTerm(i) for i in vocabularydata]
        return SimpleVocabulary(items)


Hydrochloricacid37PercentVocabularyFactory = Hydrochloricacid37PercentVocabulary()


class GlycerolVocabulary(object):
    """Vocabulary factory to pull single unfiltered data element
    Call by using (vocabulary="immunarray.lims.content.vocabulary.GlycerolVocabulary")
    """
    implements(IVocabularyFactory)

    def __call__(self, context):
        translate = context.translate
        catalog = context.portal_catalog
        proxies = catalog(
            object_provides="immunarray.lims.content.material.IGlycerol")
        vocabularydata = []
        items = []
        for proxy in proxies:
            material = proxy.getObject()
            if material.GlycerolStatus == 'Released' and material.GlycerolExpDate >= datetime.datetime.now().date():
                vocabularydata.append(material.GlycerolLot)
            items = [SimpleTerm(i) for i in vocabularydata]
        return SimpleVocabulary(items)


GlycerolVocabularyFactory = GlycerolVocabulary()


class Igg_Cy3Vocabulary(object):
    """Vocabulary factory to pull single unfiltered data element
    Call by using (vocabulary="immunarray.lims.content.vocabulary.Igg_Cy3Vocabulary")
    """
    implements(IVocabularyFactory)

    def __call__(self, context):
        translate = context.translate
        catalog = context.portal_catalog
        proxies = catalog(
            object_provides="immunarray.lims.content.material.IIgg_Cy3")
        vocabularydata = []
        items = []
        for proxy in proxies:
            material = proxy.getObject()
            if material.Igg_Cy3Status == 'Released' and material.Igg_Cy3ExpDate >= datetime.datetime.now().date():
                vocabularydata.append(material.Igg_Cy3Lot)
            items = [SimpleTerm(i) for i in vocabularydata]
        return SimpleVocabulary(items)


Igg_Cy3VocabularyFactory = Igg_Cy3Vocabulary()


class Igm_Af647Vocabulary(object):
    """Vocabulary factory to pull single unfiltered data element
    Call by using (vocabulary="immunarray.lims.content.vocabulary.Igm_Af647Vocabulary")
    """
    implements(IVocabularyFactory)

    def __call__(self, context):
        translate = context.translate
        catalog = context.portal_catalog
        proxies = catalog(
            object_provides="immunarray.lims.content.material.IIgm_Af647")
        vocabularydata = []
        items = []
        for proxy in proxies:
            material = proxy.getObject()
            if material.Igm_Af647Status == 'Released' and material.Igm_Af647ExpDate >= datetime.datetime.now().date():
                vocabularydata.append(material.Igm_Af647Lot)
            items = [SimpleTerm(i) for i in vocabularydata]
        return SimpleVocabulary(items)


Igm_Af647VocabularyFactory = Igm_Af647Vocabulary()

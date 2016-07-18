from zope import schema

from plone.supermodel import model
from zope.interface import Interface

from immunarray.lims import messageFactory as _


class ITestRequisition(model.Schema):
    """
    """

    sample_id = schema.TextLine(
        title=_(u"Sample ID"),
        required=True,
    )

    patient = schema.Choice(
        title=_(u"Patient"),
        description=_(u""),
        vocabulary=u"immunarray.lims.interfaces.patient.PatientVocabulary",
        required=True,
    )

    repeat_order = schema.Bool(
        title=_(u"Repeat Order"),
        default=False,
        required=False,
    )

    doctor = schema.Choice(
        title=_(u"Doctor"),
        description=_(u""),
        vocabulary=u"immunarray.lims.interfaces.doctor.DoctorVocabulary",
        required=True,
    )

from plone import api
from plone.supermodel import model
from zope import schema
from zope.interface import Interface
import datetime

from immunarray.lims import messageFactory as _


class ITestRequisitionFolder(Interface):
    """Folder to hold test requisitions
    """


class ITestRequisition(model.Schema):
    """
    """
    SampleID = schema.ASCIILine(
        title=_(u"Sample ID"),
        required=True,
    )
    Patient = schema.Choice(
        title=_(u"Patient"),
        description=_(u""),
        vocabulary=u"immunarray.lims.interfaces.patient.PatientVocabulary",
        required=True,
    )
    RepeatOrder = schema.Bool(
        title=_(u"Repeat Order"),
        default=False,
        required=False,
    )
    Doctor = schema.Choice(
        title=_(u"Doctor"),
        description=_(u""),
        vocabulary=u"immunarray.lims.interfaces.doctor.DoctorVocabulary",
        required=True,
    )


def TestRequisitionReceived(instance, event):
    """Add Aliquots when a 'receive' transition is fired on any sample
    """
    # creation doesn't have a 'transition'
    if not event.transition \
            or event.transition.id != 'receive':
        return

    schema = instance.Schema()

    # Aliquots are based on this number which is provided by sample supplier
    usn = schema['Unique_sample_number'].get(instance)

    alfolder = instance.aliquots

    # Create 2 Bulk Aliquots:
    bulk_aliquots = [
        api.content.create(container=alfolder, type="aliquot", id=usn + "-A01"),
        api.content.create(container=alfolder, type="aliquot", id=usn + "-B01")
    ]
    for ba in bulk_aliquots:
        ba.PourDate = datetime.date.today()
        ba.Use = u"Bulk"
        ba.Department = u"Clinical"
        ba.Volume = 2000
        ba.Status = u"Available"

    # Create -A02, -A03, -A04:
    working_aliquots = [
        api.content.create(container=alfolder, type="aliquot", id=usn + "-A02"),
        api.content.create(container=alfolder, type="aliquot", id=usn + "-A03"),
        api.content.create(container=alfolder, type="aliquot", id=usn + "-A04"),
    ]
    # We'll create working aliquots from the first bulk aliquot: -A01.
    ba = bulk_aliquots[0]
    for wa in working_aliquots:
        wa.PourDate = datetime.date.today()
        wa.Use = u"Working"
        wa.Department = u"Clinical"
        wa.Volume = 20
        wa.Status = u"Available"
        # Subtrace this twenty uL from the bulk aliquot's volum
        ba.Volume -= 20

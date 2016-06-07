import datetime
from zope import schema
from zope.interface import Interface
from zope.interface.declarations import implements

from immunarray.lims.content.person import IPerson
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary

from immunarray.lims import _

class IPatientFolder(Interface):
    """Folder to hold test requisitions
    """

class IPatient(IPerson):
    """
    """
    Firstname = schema.ASCIILine(
        title=_(u"Firstname"),
        description=_(u""),
        required=False,
    )
    Lastname = schema.ASCIILine(
        title=_(u"Lastname"),
        description=_(u""),
        required=False,
    )
    EmailAddress = schema.ASCIILine(
        title=_(u"EmailAddress"),
        description=_(u""),
        required=False,
    )
    Phone = schema.ASCIILine(
        title=_(u"Phone number"),
        description=_(u""),
        required=False,
    )

class PatientVocabulary(object):
    """List existing patients
    """
    implements(IVocabularyFactory)
    def __call__(self, context):
        catalog = context.portal_catalog
        proxies = catalog(
            object_provides="immunarray.lims.content.patient.IPatient")
        vocabularydata = []
        items=[]
        for proxy in proxies:
            instance = proxy.getObject()
            vocabularydata.append(instance.id)
            items = [SimpleTerm(i) for i in vocabularydata]
        return SimpleVocabulary(items)


PatientVocabularyFactory = PatientVocabulary()

from datetime import date
from plone.app.textfield import RichText
from zope import schema
from immunarray.lims import messageFactory as _
from plone.dexterity.utils import createContentInContainer
from bika.lims.interfaces.sample import ISample
from plone.autoform import directives
from z3c.form.browser.radio import RadioFieldWidget


class IVeracisRunBase(model.Schema):
    """Object that will be the base of all veracis runs
    """
    veracis_run_number = schema.Int(
        title=_(u"Veracis Run Number"),
        description=_(u"Veracis Run Number"),
        required=True,
    )
    veracis_run_purpose = schema.TextLine(
        title=_(u"Veracis Test Run Purpose"),
        description=_(u"Veracis Test Run Purpose"),
    )
    veracis_run_serial_number = schema.Int(
        title=_(u"Veracis Run Serial Number"),
        description=_(u"Veracis Run Serial Number"),
    )
    veracis_test_run_date=schema.Date(
        title=_(u"Veracis Test Run Date"),
        description=_(u"Veracis Test Run Date"),
    )
    veracis_test_scan_date=schema.Date(
        title=_(u"Veracis Test Scan Date"),
        description=_(u"Veracis Test Scan Date"),
    )

alsoProvides( IFormFieldProvider)

# -*- coding: utf-8 -*-
from datetime import date
from immunarray.lims.interfaces.veracisrunbase import IVeracisRunBase
from z3c.form import button
from z3c.form.form import EditForm
"""Add buttons to a form don't think it goes in the interface!"""
class Form(EditForm):
    @button.buttonAndHandler(
        u"Commercail Run",
        name="CommercalRun",
        condition=lambda form: form.okToDelete()
    )
    def handleDelete(self, action):
        """
            Delete this event.
        """
        pass
        self.status = "Event deleted."

class IEightFrameRun(IVeracisRunBase):
    """Eight well iChip test run
    """
    # aliquots go on iChip
    # iChips go into test run
    # test form is how the data will be interacted with!
    pass

"""
fields from base object
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
veracis_run_operator = schema.TextLine(
    title=_(u"Veracis Run Operator"),
    description=_(u"Veracis Run Operator"),
    required=True,
)
veracis_test_run_date = schema.Date(
    title=_(u"Veracis Test Run Date"),
    description=_(u"Veracis Test Run Date (MM/DD/YYYY)"),
    default=date.today(),
)
veracis_test_scan_date = schema.Date(
    title=_(u"Veracis Test Scan Date"),
    description=_(u"Veracis Test Scan Date (MM/DD/YYYYY)"),
    default=date.today(),
)
pdf_veracis_run = NamedBlobImage(
    title=_(u"PDF Upload of Test Form"),
    description=_(u"PDF Upload of Test Form"),
    required=False,
)

alsoProvides(IVeracisRunBase, IFormFieldProvider)
"""

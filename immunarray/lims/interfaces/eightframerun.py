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
    pass

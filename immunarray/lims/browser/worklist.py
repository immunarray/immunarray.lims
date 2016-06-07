from collective.z3cform.datagridfield import DataGridFieldFactory
from immunarray.lims.interfaces.worklist import IWorklist
from plone.directives.form import form

from z3c.form import field
from z3c.form.form import extends


class WorklistEditForm(form.EditForm):
    extends(form.EditForm)

    fields = field.Fields(IWorklist)
    label = u"Worklist"

    fields['TestForm'].widgetFactory = DataGridFieldFactory
    fields['Solutions'].widgetFactory = DataGridFieldFactory

    def updateWidgets(self):
        super(WorklistEditForm, self).updateWidgets()
        self.widgets['TestForm'].allow_insert = False
        self.widgets['TestForm'].allow_delete = False
        self.widgets['TestForm'].auto_append = True
        self.widgets['TestForm'].allow_reorder = False
        # self.widgets['TestForm'].main_table_css_class = 'some-class'
        self.widgets['Solutions'].allow_insert = False
        self.widgets['Solutions'].allow_delete = False
        self.widgets['Solutions'].auto_append = False
        self.widgets['Solutions'].allow_reorder = False
        # self.widgets['Solutions'].main_table_css_class = 'some-class'

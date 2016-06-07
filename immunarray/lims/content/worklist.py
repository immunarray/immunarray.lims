from plone.directives import form
from z3c.form.form import extends
from z3c.form import field
from plone.directives import form

from collective.z3cform.datagridfield import DictRow, DataGridFieldFactory

from immunarray.lims import _
from zope.interface import Interface
from zope import schema


class IWorklistFolder(Interface):
    """Folder to hold worklists
    """


class ITestFormTableRowSchema(form.Schema):
    """A single row in the TestForm table
    """
    sequence = schema.TextLine(
        title=u"Sequence",
        readonly=True)
    scan_slot = schema.TextLine(
        title=u"Scan Slot",
        required=False)
    check_one = schema.TextLine(
        title=u"Confirm Sample in Well Position",
        required=False)
    slide_id = schema.TextLine(
        title=u"Slide ID/well position",
        required=False)
    check_two = schema.TextLine(
        title=u"Confirm Chip in Correct Scanning Position",
        required=False)
    specimen_id = schema.TextLine(
        title=u"Specimen ID",
        required=False)
    aliquot_id = schema.TextLine(
        title=u"Aliquot ID",
        required=False)
    comments = schema.TextLine(
        title=u"Comments",
        required=False)


TESTFORM_DEFAULT = [
    {'sequence': '%s' % x,
     'scan_slot': '',
     'check_one': False,
     'slide_id': '',
     'check_two': False,
     'specimen_id': '',
     'aliquot_id': '',
     'comments': '',
     } for x in range(1, 37)]


class ISolutionsTableRowSchema(form.Schema):
    """A single row in the TestForm table
    """
    solutions = schema.TextLine(
        title=u"Solutions",
        readonly=True)
    batch_number = schema.TextLine(
        title=u"Batch #",
        required=False)
    expiration_date = schema.Date(
        title=u"Expiration Date",
        required=False)


SOLUTIONS_DEFAULT = [
    {'solutions': 'Reverse Osmosis Water',
     'batch_number': '',
     'expiration_date': None,
     },
    {'solutions': '10X PBS',
     'batch_number': '',
     'expiration_date': None,
     },
    {'solutions': '1X PBS',
     'batch_number': '',
     'expiration_date': None,
     },
    {'solutions': '1X PBS - 22.4% Tween 20',
     'batch_number': '',
     'expiration_date': None,
     },
    {'solutions': '1X PBS 1% Casein',
     'batch_number': '',
     'expiration_date': None,
     },
    {'solutions': 'GahulgG-Cy3 in 50% Glycerol',
     'batch_number': '',
     'expiration_date': None,
     },
    {'solutions': 'GahulgM-AF647 in 50% Glycerol',
     'batch_number': '',
     'expiration_date': None,
     },
    {'solutions': '70% Ethanol',
     'batch_number': '',
     'expiration_date': None,
     },
]


class IWorklist(Interface):
    """The main Worklist schema
    """
    DocumentNumber = schema.ASCIILine(
        title=_(u"Run Number"),
        description=_(u"Veracis Run Number"),
        required=True,
    )
    Assay = schema.ASCIILine(
        title=_(u"Assay"),
        description=_(u""),
        required=True,
    )
    TestDate = schema.Date(
        title=_(u"Date of Test"),
        description=_(u"Date of Test Run"),
        required=True,
    )
    ScanDate = schema.Date(
        title=_(u"Date of Scan"),
        description=_(u"Date of Scanning"),
        required=True,
    )
    TestForm = schema.List(
        title=u"Test Form",
        value_type=DictRow(title=u"test", schema=ITestFormTableRowSchema),
        required=True,
        default=TESTFORM_DEFAULT
    )
    Solutions = schema.List(
        title=u"Solutions",
        value_type=DictRow(title=u"solution", schema=ISolutionsTableRowSchema),
        required=True,
        default=SOLUTIONS_DEFAULT
    )


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

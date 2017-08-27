# -*- coding: utf-8 -*-
from collective.z3cform.datagridfield import DictRow
from immunarray.lims import messageFactory as _
from plone.directives import form
from zope import schema
from zope.interface import Interface


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

    document_number = schema.TextLine(
        title=_(u"Run Number"),
        description=_(u"Veracis Run Number"),
        required=True,
    )

    test_form = schema.List(
        title=u"Test Form",
        value_type=DictRow(title=u"test", schema=ITestFormTableRowSchema),
        required=True,
        default=TESTFORM_DEFAULT
    )

    solutions = schema.List(
        title=u"Solutions",
        value_type=DictRow(title=u"solution", schema=ISolutionsTableRowSchema),
        required=True,
        default=SOLUTIONS_DEFAULT
    )

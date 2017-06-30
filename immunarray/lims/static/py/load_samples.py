#!/usr/bin/env python

import os
import xlrd
import timeit
from Tkinter import Tk
from tkFileDialog import askopenfilename
from datetime import datetime, date
#from plone.api.content import create
#import transaction
#from DateTime import DateTime

print "Pick Specimen Database"
Tk().withdraw()
filename = askopenfilename(initialdir = "/home/jpitts/Desktop")
# MM-002.02 (specimen database)
workbook_MM_002_02 = xlrd.open_workbook(filename, encoding_override="cp1252", on_demand = True)
CS = workbook_MM_002_02.sheet_by_name('Clinical Samples (CS)')
DS = workbook_MM_002_02.sheet_by_name('Development Cohorts (DC)')
RS = workbook_MM_002_02.sheet_by_name(' Reference Standards (RS)')
SP_AC = workbook_MM_002_02.sheet_by_name('Specimen Accessioning')
Box_Location = workbook_MM_002_02.sheet_by_name(' Box Location')

print "Pick Patient Database"
Tk().withdraw()
filename2 = askopenfilename(initialdir = "/home/jpitts/Desktop")
workbookPP_014_03 = xlrd.open_workbook(filename2,encoding_override="cp1252", on_demand = True)
Patient = workbookPP_014_03.sheet_by_name('Patient')


start= timeit.default_timer()

# import pdb;pdb.set_trace()
# Make Patient Records
# Watch for repeat patients and missing names/dobs
# Make Sample Records
# Need to know what test was ordered so that the correct Assay is applied
# Make Aliquot Records
# Need to be sure the bulks are made then the child objects,
# also need to figure out how to attach the results

stop = timeit.default_timer()
print "Run Time " + (stop - start)

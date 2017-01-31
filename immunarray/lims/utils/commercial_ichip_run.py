# -*- coding: utf-8 -*-
from datetime import date
from plone.api.content import create
from immunarray.lims.interfaces import ichip
from immunarray.lims.interfaces import ichiplot
from immunarray.lims.interfaces import commercial_eight_frame_run
from immunarray.lims.interfaces import ichipassay

#sample selection
#aliquot selection

#query to close iChipLots, and make changes based on inventory
#reasons to close a lot
#ichiplot.expiration_date is greater than current date
#ichip count of any lot less than 1

#set var iChipLot_Count
#set var max_iChipLots

#query iChipLots with "Passed" status, count results

#if loop for count >=10
    #make list with oldest first based on ichiplot.print_date
    #of
#than loop for count <10

#query iChipLots that have "Passed" (want the oldest, based on ichiplot.print_date)

#count iChips in "Released" state

#if loop for count% by number of ichipassay.number_of_same_lot_replication_needed_for_samples

    #save iChipLot and Chips to use (Lot, ichip.title)
    #add 1 to iChipLot_Count

#than loop, subtract 1 from count of iChips

#set var plate_count=0

def SelectiChips(event):
    pass


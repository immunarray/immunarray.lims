# -*- coding: utf-8 -*-
from plone import api
import datetime


def Received(instance, event):
    """Add Aliquots when a 'receive' transition is fired on a Test Requisition
    """
    # Fires on all Transition events including creation
    if not event.transition or event.transition.id != 'receive':
        return

    schema = instance.Schema()

    # Aliquots are based on this number which is provided by sample supplier
    usn = instance.USN
    folder = instance.folder  # use acquisition to override storage location!

    # Create 2 Bulk Aliquots:
    bulk_aliquots = [
        api.content.create(container=folder, type="aliquot", id=usn + "-A01"),
        api.content.create(container=folder, type="aliquot", id=usn + "-B01")
    ]
    for ba in bulk_aliquots:
        ba.PourDate = datetime.date.today()
        ba.Use = u"Bulk"
        ba.Department = u"Clinical"
        ba.Volume = 2000
        ba.Status = u"Available"

    # Create -A02, -A03, -A04:
    working_aliquots = [
        api.content.create(container=folder, type="aliquot", id=usn + "-A02"),
        api.content.create(container=folder, type="aliquot", id=usn + "-A03"),
        api.content.create(container=folder, type="aliquot", id=usn + "-A04"),
    ]
    # We'll create working aliquots from the first bulk aliquot: -A01.
    ba = bulk_aliquots[0]
    for wa in working_aliquots:
        wa.PourDate = datetime.date.today()
        wa.Use = u"Working"
        wa.Department = u"Clinical"
        wa.Volume = 20
        wa.Status = u"Available"
        # Subtract this twenty uL from the bulk aliquot's volume
        ba.Volume -= 20

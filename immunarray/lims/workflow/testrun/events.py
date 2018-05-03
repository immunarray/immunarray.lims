from immunarray.lims.interfaces.assayrequest import IAssayRequest
from immunarray.lims.interfaces.clinicalaliquot import IClinicalAliquot
from immunarray.lims.interfaces.clinicalsample import IClinicalSample
from immunarray.lims.interfaces.ichip import IiChip
from immunarray.lims.interfaces.qcaliquot import IQCAliquot
from plone.api.content import find, transition


def after_queue(instance):
    """
    """
    assayrequests, clinicalaliquots, ichips, qcaliquots = run_objects(instance)
    for obj in set(qcaliquots):
        transition(obj, "queue")
    for obj in set(clinicalaliquots):
        transition(obj, "queue")
    for obj in set(ichips):
        transition(obj, "queue")
    for obj in set(assayrequests):
        transition(obj, "queue")


def after_begin_process(instance):
    """
    """
    assayrequests, clinicalaliquots, ichips, qcaliquots = run_objects(instance)
    for obj in set(qcaliquots):
        transition(obj, "begin_process")
    for obj in set(clinicalaliquots):
        transition(obj, "begin_process")
    for obj in set(assayrequests):
        transition(obj, "begin_process")


def after_result(instance):
    """
    """


def after_cancel_run(instance):
    """When cancelling a test run, objects that were linked here must
    be freed for use in a future test run, or cancelled.
    - cancels iChip and Aliquot objects
    - make_available on AssayRequest objects.
    """
    assayrequests, clinicalaliquots, ichips, qcaliquots = run_objects(instance)
    for obj in set(qcaliquots):
        transition(obj, "make_available")
    for obj in set(clinicalaliquots):
        transition(obj, "make_available")
    for obj in set(ichips):
        transition(obj, "make_available")
    for obj in set(assayrequests):
        transition(obj, "make_available")


def after_abort_run(instance):
    """There are only one type of object supporting abort, and that is the
    Test Run itself.  So, I guess we don't abort any other objects here when
    the run is aborted.
    """
    # XXX: need a way to show aborted links in the UI


def get_assayrequest_from_aliquot(aliquot):
    sample = aliquot.aq_parent
    while not IClinicalSample.providedBy(sample):
        if not hasattr(sample, 'aq_parent'):
            return None
        sample = sample.aq_parent
    for child in sample.objectValues():
        if IAssayRequest.providedBy(child):
            return child


def run_objects(instance):
    clinicalaliquots = []
    qcaliquots = []
    ichips = []
    assayrequests = []
    for plate in instance.plates:
        for key, value in plate.items():
            brains = find(UID=value)
            if brains:
                obj = brains[0].getObject()
            _items = qcaliquots + clinicalaliquots + ichips + assayrequests
            if not obj or obj in _items:
                continue
            if IiChip.providedBy(obj):
                ichips.append(obj)
            elif IQCAliquot.providedBy(obj):
                qcaliquots.append(obj)
            elif IClinicalAliquot.providedBy(obj):
                clinicalaliquots.append(obj)
                # get assayrequest
                ar = get_assayrequest_from_aliquot(obj)
                assayrequests.append(ar)
    return assayrequests, clinicalaliquots, ichips, qcaliquots

from immunarray.lims import logger
from immunarray.lims.interfaces.assayrequest import IAssayRequest
from immunarray.lims.interfaces.clinicalaliquot import IClinicalAliquot
from immunarray.lims.interfaces.clinicalsample import IClinicalSample
from immunarray.lims.interfaces.ichip import IiChip
from immunarray.lims.interfaces.qcaliquot import IQCAliquot
from plone.api.content import find, transition


def after_queue(instance):
    """
    """


def after_begin_process(instance):
    """
    """


def after_result(instance):
    """
    """


def after_report(instance):
    """
    """


def after_wet_work_done(instance):
    """
    """


def after_scanning(instance):
    """
    """


def get_assayrequest_from_aliquot(aliquot):
    sample = aliquot.aq_parent
    while not IClinicalSample.providedBy(sample):
        if not hasattr(sample, 'aq_parent'):
            return None
        sample = sample.aq_parent
    for child in sample.objectValues():
        if IAssayRequest.providedBy(child):
            return child


def after_cancel_run(instance):
    """When cancelling a test run, objects that were linked here must
    be freed for use in a future test run, or cancelled.
    - cancels iChip and Aliquot objects
    - make_available on AssayRequest objects.
    """
    clinicalaliquots = []
    qcaliquots = []
    ichips = []
    assayrequests = []

    for plate in instance.plates:
        for key, value in plate.items():
            obj = get_object(value)
            _items = qcaliquots + clinicalaliquots + ichips + assayrequests
            if not obj or obj in _items:
                continue
            # ichip
            if IiChip.providedBy(obj):
                ichips.append(obj)
            # aliquot
            elif IQCAliquot.providedBy(obj):
                qcaliquots.append(obj)
            elif IClinicalAliquot.providedBy(obj):
                clinicalaliquots.append(obj)
                # get assayrequest
                ar = get_assayrequest_from_aliquot(obj)
                assayrequests.append(ar)

    for obj in set(qcaliquots):
        logger.info("transitioning %s with make_available" % obj)
        transition(obj, "make_available")

    for obj in set(clinicalaliquots):
        logger.info("transitioning %s with make_available" % obj)
        transition(obj, "make_available")

    for obj in set(ichips):
        logger.info("transitioning %s with make_available" % obj)
        transition(obj, "make_available")

    for obj in set(assayrequests):
        logger.info("transitioning %s with make_available" % obj)
        transition(obj, "make_available")


def after_abort_run(instance):
    """There are only one type of object supporting abort, and that is the
    Test Run itself.  So, I guess we don't abort any other objects here when
    the run is aborted.
    """
    # XXX: need a way to show aborted links in the UI


def get_object(uid):
    brains = find(UID=uid)
    if brains:
        return brains[0].getObject()

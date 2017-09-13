# -*- coding: utf-8 -*-


class InvalidAssaySelected(Exception):
    """Selected iChip Assay not found
    """


class NoIchipLotsFound(Exception):
    """No iChipLots Found
    """


class NotEnoughUniqueIChipLots(Exception):
    """Not enough unique iChipLots found
    """


class QCSampleNotFound(Exception):
    """QC Sample not found
    """


class QCAliquotNotFound(Exception):
    """Available QC Aliquots meeting assay parameters not found
    """


class NoWorkingAliquotsFound(Exception):
    """No working aliquots found
    """


class ObjectInInvalidState(Exception):
    """At least one object is in an invalid state!  Re-create the run
    """


class DuplicateWellSelected(Exception):
    """You cannot use the same well number twice on a single plate
    """


class InvalidSample(Exception):
    """The sample is not Clinical, HQC, or LQC, so we cannot use it
    """


class MissingIChipForSlide(Exception):
    """The IChip ID is invalid, or blank, but aliquots exist
    """

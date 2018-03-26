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


def get_serializeArray_form_values(request):
    """Parse the form_values list into a single dictionary.
    The plates are taken care of particularly, like this:

    {'thing1': 'value1',
     'thing2': 'value2'...
     'plates': [
         {plate1-stuff}, 
         {plate2-stuff}
     ]
    }
    """
    raw = request.form
    count = len([x for x in raw if 'form_values' in x])
    nr_plates = 0

    # gather intermediate data dictionary
    intermediate = {}
    for x in range(0, count / 2):
        name = raw['form_values[%s][name]' % x]
        value = raw['form_values[%s][value]' % x]
        if name in intermediate:
            if type(intermediate[name]) == list:
                intermediate[name].append(value)
            else:
                intermediate[name] = [intermediate[name], value]
            nr_plates = len(intermediate[name])
        else:
            intermediate[name] = value

    # Separate the plates from the rest of the form values, and convert
    # them to a single list of dictionaries. any key in the form who's
    # name starts with one plate_keys, will be included in the "plates"
    # element of the returned list
    plate_keys = ['chip-', 'comments', 'scan-slot', 'well-number']
    plates = [{} for x in range(nr_plates+1)]
    form_values = {}
    for k, v in intermediate.items():
        if any([k.startswith(pk) for pk in plate_keys]):
            if not isinstance(v, (list, tuple)):
                v = [v]
            for nr in range(nr_plates+1):
                plates[nr][k] = v[nr]
        else:
            form_values[k] = v

    form_values['plates'] = plates
    return form_values

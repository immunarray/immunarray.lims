# -*- coding: utf-8 -*-
import json
import traceback
from datetime import datetime
from operator import itemgetter

import transaction
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from immunarray.lims.browser.testrun import DuplicateWellSelected, \
    InvalidAssaySelected, NoIchipLotsFound, NoWorkingAliquotsFound, \
    NotEnoughUniqueIChipLots, ObjectInInvalidState, QCAliquotNotFound, \
    QCSampleNotFound, get_serializeArray_form_values, transition_plate_contents
from immunarray.lims.interfaces import ITestRuns
from immunarray.lims.interfaces.aliquot import IAliquot
from immunarray.lims.interfaces.assayrequest import IAssayRequest
from immunarray.lims.interfaces.clinicalsample import IClinicalSample
from immunarray.lims.interfaces.ichip import IiChip
from immunarray.lims.interfaces.ichipassay import IiChipAssay
from immunarray.lims.interfaces.sample import ISample
from immunarray.lims.interfaces.veracisrunbase import IVeracisRunBase
from immunarray.lims.vocabularies.ichipassay import IChipAssayListVocabulary
from immunarray.lims.vocabularies.users import LabUsersUserVocabulary
from plone.api.content import create, find, get_state, transition
from plone.api.exc import InvalidParameterError
from plone.api.portal import get_tool


class CreateTestRunView(BrowserView):
    template = ViewPageTemplateFile("templates/testrun_create.pt")

    def __init__(self, context, request):
        BrowserView.__init__(self, context, request)
        self.context = context
        self.request = request
        self.errors = []

    def __call__(self):
        request = self.request

        try:

            if request.form.get("ctest_action", "") == 'selected_an_assay':
                plates = self.selected_an_assay()
                solution_batches = self.get_assay_solutions()
                return json.dumps({'success': True,
                                   'TestRun': plates,
                                   'solution_batches': solution_batches})

            elif request.form.get('ctest_action', '') == 'save_run':
                run = self.save_run()
                return json.dumps(
                    {'success': True,
                     'redirect_url': run.absolute_url() + '/view'})

        except Exception as e:

            msg = "<br/>" + traceback.format_exc().split("\n", 1)[-1]
            msg = msg.replace("\n", "<br/>").replace(" ", "&nbsp;&nbsp;")
            transaction.abort()
            return json.dumps({'success': False, 'message': msg})

        return self.template()

    @property
    def assay_name(self):
        """get assay name from the form, or from self.context for edit views
        """
        if 'assay_name' not in self.request \
                and not hasattr(self.context, 'assay_name'):
            return None

        assay_name = self.request.get('assay_name', None)
        if not assay_name and not ITestRuns.providedBy(self.context):
            assay_name = self.context.assay_name
        if not assay_name:
            raise InvalidAssaySelected(self.assay_name)
        return assay_name

    def next_veracis_run_number(self):
        """Get the highest run_number of all runs (of all types of run),
        increment it and return.
        """
        catalog = get_tool('portal_catalog')
        try:
            cur_nr = catalog(object_provides=IVeracisRunBase.__identifier__,
                             sort_on='run_number',
                             sort_order='reverse',
                             limit=1)[0].run_number
            return int(cur_nr) + 1
        except IndexError:
            return '1'

    def lab_users(self):
        items = LabUsersUserVocabulary(self).by_value.values()
        return [(i.value, i.title) for i in items]

    def iChipAssayList(self):
        vocab_keys = IChipAssayListVocabulary.__call__(self).by_value.keys()
        return vocab_keys

    def get_assay_solutions(self):
        """Dynamically return a list of possible batches, for each type of
        solution required by the assay
        """
        vocabs = []
        assay = self.get_assay()
        if not assay:
            return vocabs
        if assay.needed_solutions:
            for solution_type_name in assay.needed_solutions:
                type_batches = find(Type=solution_type_name,
                                    expires={'query': datetime.today().date(),
                                             'range': 'min'},
                                    sort_on='expires')

                tmp = []
                for batch in type_batches:
                    tmp.append([batch.id,
                                batch.Title,
                                batch.expires.strftime('%Y-%m-%d')])
                vocabs.append([solution_type_name, tmp])
        return vocabs

    def selected_an_assay(self):
        if self.assay_name == 'None':
            return self.template()
        elif self.assay_name == 'Custom':
            pass
        else:
            assay = self.get_assay()
            if assay.desired_use == 'Commercial':
                plates = self.makeTestPlan(assay)
                return plates
            if assay.desired_use == 'Development':
                pass

    def get_assay(self):
        assay_name = self.assay_name
        if assay_name:
            brains = find(portal_type='iChipAssay', Title=assay_name)
            if not brains:
                raise InvalidAssaySelected(self.assay_name)
            return brains[0].getObject()

    def maxNumberOfSamplesToRun(self, assay):
        """take the assay parameters and determine the max number of samples
        that can be tested in a single run
        """
        max_plates = assay.max_number_of_plates_per_test_run
        hqc = assay.number_of_high_value_controls
        lqc = assay.number_of_low_value_controls
        number_same_lot = assay.number_of_same_lot_replication_needed
        number_unique_lot = assay.number_of_unique_ichips_lots_needed
        frame_count = assay.framecount
        # update type to be frame type (int)
        wells_needed_per_sample = number_same_lot * number_unique_lot
        max_wells = max_plates * frame_count
        testing_wells_for_hqc = wells_needed_per_sample * hqc
        testing_wells_for_lqc = wells_needed_per_sample * lqc
        sample_wells = max_wells - (
            testing_wells_for_hqc + testing_wells_for_lqc)
        max_samples_to_test = sample_wells - wells_needed_per_sample
        return max_samples_to_test

    def queryClinicalSamples(self, assay):
        """Get all the samples that are review_state='received', and which
        contain an "AssayRequest" who's title matches the assay_name, and who
        have a review_state of (re_run or to_be_tested).
        """
        sample_data = []
        for testable_state in ['re_run', 'to_be_tested']:
            # this does get Clinical Samples keep reading jp
            brains = find(portal_type="AssayRequest",
                          Title=assay.title,
                          review_state=testable_state)
            tmp = []
            for brain in brains:
                assay_request = brain.getObject()
                sample = assay_request.aq_parent
                tmp.append({'uid': sample.UID(),
                            'draw_date': sample.collection_date,
                            'test_status': get_state(assay_request),
                            'sample': sample})
            tmp = sorted(tmp, key=itemgetter('draw_date'))
            sample_data.extend(tmp)

        max_nr_samples = self.maxNumberOfSamplesToRun(assay)
        return sample_data[:max_nr_samples]

    def queryClinicalWorkingAliquots(self, assay):
        """Query to get QC and Clinical working aliquots to test with.
        """
        aliquots = []
        # loop over all the samples coming into search
        clinical_samples = self.queryClinicalSamples(assay)
        for sample_dict in clinical_samples:
            parent = sample_dict['sample']  # parent is sample object
            tmp = self.collectAliquots(
                parent,
                Type='Clinical Aliquot (Working)',
                review_state='available',
                remaining_volume={
                    'query': assay.desired_working_aliquot_volume,
                    'range': 'min'},
            )
            # we only want a single aliquot from those found.
            if tmp:
                aliquots.append(tmp[0])
        if not aliquots:
            samples = [sd['sample'] for sd in clinical_samples]
            msg = "Searched in clinical samples: {}".format(",".join(samples))
            raise NoWorkingAliquotsFound(msg)
        return aliquots

    def collectAliquots(self, sample_object, **kwargs):
        """Get in array of objects to see if they are the last in the chain
        and return a list of objects back.  Check if each is a working aliquot
        that meets the needs of the assay
    
        Type is the value of the index called 'Type'.  It's set (for aliquots)
        in the adapters/indexers.py.
        """
        path = '/'.join(sample_object.getPhysicalPath())
        brains = find(path={'query': path, 'depth': -1},
                      sort_on='id',
                      **kwargs)
        items = [b.getObject() for b in brains]
        return items

    def makeTestPlan(self, assay):
        """use ordered [ichiplot, [ichips]], assay parameters{},
        [working aliquots] to build test plan
    
        """
        max_plates = assay.max_number_of_plates_per_test_run
        number_same_lot = assay.number_of_same_lot_replication_needed
        number_unique_lot = assay.number_of_unique_ichips_lots_needed
        frame_count = assay.framecount

        ichips_for_assay = self.getiChipsForTesting(assay)
        working_aliquots = self.queryClinicalWorkingAliquots(assay)
        number_of_ichip_lots_available = len(ichips_for_assay)

        if not number_of_ichip_lots_available >= number_unique_lot:
            msg = "Assay requires %s unique lots" % number_unique_lot
            raise NotEnoughUniqueIChipLots(msg)

        plate_count = 0
        _used_ichiplots = []
        _used_ichips = []
        result = []  # thing that will be sent back each entry is a "plate"

        # condition that lets me know to keep making plates both parts must
        # be true
        while plate_count <= max_plates and len(working_aliquots) > 0:
            # add QC to working_aliquots is no ichiplots have been used
            if not _used_ichiplots:
                qc_list = self.getQCAliquots(assay)
                for qc in qc_list:
                    working_aliquots.insert(0, qc)
            active_lots = []
            required_ichips_for_testing = []
            for xx in ichips_for_assay:
                ichiplot, ichips = xx
                # That tells me if we have used this lot before
                if ichiplot.title.split(".")[0] not in (
                        active_lots[j][0].title.split(".")[0] for j in
                        range(len(active_lots))):
                    # faulty because we don't update the ichips,
                    # if true once it will always be true!
                    if len(ichips) >= number_same_lot:
                        if ichiplot not in _used_ichiplots:
                            active_lots.append(xx)
                            _used_ichiplots.append(ichiplot)
                        elif ichiplot in _used_ichiplots:
                            lot_chip_count = 0  # Running chip count in this lot
                            for chip in _used_ichips:
                                if chip.getParentNode() == ichiplot:
                                    lot_chip_count += 1  # count
                                    # of how many ichips have been used from
                                    # current lot
                            if len(ichips) - lot_chip_count >= number_same_lot:
                                active_lots.append(xx)
                # Need to account for how many ichips are left in the lot and
                # if len(list_of_ichip_objects)-len(_used_ichips from that lot)
                #  > number_same_lot
                if len(active_lots) == number_unique_lot:
                    # have the ichiplots selected for the current set of
                    # sample slots
                    for lot in _used_ichiplots:
                        if lot in (active_lots[i][0] for i in
                                   range(number_unique_lot)):
                            continue  # Using the same lot as in a previous
                            # run, no new qc needed
                        else:
                            qc_list = self.getQCAliquots(assay)
                            for qc in qc_list:
                                working_aliquots.insert(0, qc)
                            break  # we know at least one lot is new and as such
                            #  we need to run qc on the current set of samples
                    break
            # Code section to select iChips
            # number_same_lot
            for a in active_lots:
                # ichiplot = a[0]
                ichips = a[1]
                j = []
                # active_lots has the needed number of ichiplots, and has
                # enough chips for at least one pass!
                if plate_count != 0:
                    for ichip in ichips:
                        if ichip in _used_ichips:
                            continue
                        else:
                            j.append(ichip)
                            _used_ichips.append(ichip)
                            if len(j) == number_same_lot:
                                break
                    for d in j:
                        required_ichips_for_testing.append(d)
                if plate_count == 0:
                    required_ichips_for_testing.extend(ichips[:number_same_lot])
                    _used_ichips.extend(ichips[:number_same_lot])

            # a this point we have a selection of ichips, we now need to get
            # samples to be run on them.
            # Pick QC to run on ichips in the plate, will need to do this if and
            # when ichip lots change
            # make variable
            # sample slots (max of *) want to make it dynamic range(
            # 1:frame_count)
            # wrap this in an if statement
            sample_slots = []
            for i in range(frame_count):
                if working_aliquots:
                    sample_slots.append(working_aliquots[0])
                    working_aliquots = working_aliquots[1:]
            # We have the objects to this point, shoudn't we send the id's to
            #  the GUI,
            # but keep the objects in variables that can be used when the
            # user confirms the run?
            # I think it will save time of looking all this up again
            sample_ids = [x.id for x in sample_slots]
            # XXX Use residual slots for aliquots from Under Review QC samples.
            result.append(
                [[x.id, sample_ids] for x in required_ichips_for_testing])
            plate_count += 1

        return result

    def getQCSampleObject(self, veracis_id):
        """input veracis_id, get qc sample object
        """
        brains = find(portal_type='QCSample',
                      review_state='in_use',
                      veracis_id=veracis_id)
        if not brains:
            raise QCSampleNotFound("Veracis ID: %s" % veracis_id)
        return brains[0].getObject()

    def getQCAliquots(self, assay):
        """Get QC's aliquots
        """
        hqc_sample = self.getQCSampleObject(assay.qc_high_choice)
        lqc_sample = self.getQCSampleObject(assay.qc_low_choice)

        aliquots = self.collectAliquots(
            hqc_sample,
            Type='QC Aliquot (Working)',
            remaining_volume={'query': assay.minimum_working_aliquot_volume,
                              'range': 'min'},
            review_state='available'
        )
        if not aliquots:
            raise QCAliquotNotFound("HQC Sample: %s" % hqc_sample)
        hqc_aliquot = aliquots[0]

        aliquots = self.collectAliquots(
            lqc_sample,
            Type='QC Aliquot (Working)',
            remaining_volume={'query': assay.minimum_working_aliquot_volume,
                              'range': 'min'},
            review_state='available'
        )
        if not aliquots:
            raise QCAliquotNotFound("HQC Sample: %s" % hqc_sample)
        lqc_aliquot = aliquots[0]

        qc_to_add_to_plate = [hqc_aliquot] * assay.number_of_high_value_controls
        qc_to_add_to_plate += [lqc_aliquot] * assay.number_of_low_value_controls
        return qc_to_add_to_plate

    def getiChipsForTesting(self, assay):
        """Get ALL iChips that can be used for the selected assay
        [[<iChipLotID>,[<iChip>,<iChip>,<iChip>]]]
        """
        ichips_for_assay = []

        brains = find(portal_type='iChipLot',
                      review_state='released',
                      sort_on='expires')
        if not brains:
            raise NoIchipLotsFound

        ichiplots = []
        for brain in brains:
            ichiplot = brain.getObject()
            if assay.title in ichiplot.intended_assay \
                    and int(ichiplot.frames) == int(assay.framecount):
                # commercial needs, correct assay
                # want to order the ichiplots in this list by exp date
                ichiplots.append(ichiplot)

        for ichiplot in ichiplots:
            ichips = ichiplot.objectValues()
            filtered = [ic for ic in ichips if get_state(ic) == 'released']
            ichips_for_assay.append([ichiplot, filtered])

        return ichips_for_assay

    def save_run(self):
        """Create initial run
        """

        values = get_serializeArray_form_values(self.request)

        try:
            assay = find(object_provides=IiChipAssay.__identifier__,
                         Title=values['assay_name'])[0].getObject()
        except IndexError:
            raise InvalidAssaySelected(values['assay_name'])

        plates, ichips, aliquots = self.transmogrify_inputs(values['plates'])
        plates = self.remove_empty_plates(plates)
        plates = self.reorder_plates(plates)

        solutions = [values[x] for x in values if x.startswith('solution-')]

        transition_plate_contents(ichips, aliquots, 'queue')
        lab_users = LabUsersUserVocabulary(self).by_value
        planner = lab_users.get(values['run_planner'], '')
        operator = lab_users.get(values['run_planner'], '')

        brain = find(object_provides=ITestRuns.__identifier__)[0]
        folder = brain.getObject()

        try:
            run_number = int(values['run_number'])
        except (ValueError, TypeError):
            raise TypeError("Run number must be a number.")

        run = create(
            folder,
            'TestRun',
            title=values['assay_name'],
            assay_name=assay.title,
            assay_uid=assay.UID(),
            run_number=run_number,
            run_date=values['run_date'],
            run_planner=planner.title if planner else '',
            run_operator=operator.title if operator else '',
            plates=plates,
            solutions=solutions
        )
        return run

    def transmogrify_inputs(self, plates):
        """Convert titles to UIDs for all ichips and aliquots
        """
        ichips, aliquots = [], []
        # A single plate run must be converted to a list of plates
        if isinstance(plates, dict):
            plates = [plates]
        for plate in plates:
            for chip_nr in range(1, 5):
                for well_nr in range(1, 9):
                    key = "chip-{}_well-{}".format(chip_nr, well_nr)
                    if plate.get(key, False):
                        brains = find(object_provides=IAliquot.__identifier__,
                                      Title=plate[key])
                        plate[key] = brains[0].UID
                        aliquots.append(brains[0].getObject())
                key = "chip-id-{}".format(chip_nr)
                if plate.get(key, False):
                    brains = find(object_provides=IiChip.__identifier__,
                                  Title=plate[key])
                    plate[key] = brains[0].UID
                    ichips.append(brains[0].getObject())

        return plates, ichips, aliquots

    def reorder_plates(self, plates):
        """Maybe user selected new well numbers for existing plate.
        This changes the order of the plates, and passes them back.
        """
        # Re-order the well-numbers of aliquots according to the "well-number"
        # This allows analyst to re-order wells if aliquots were transposed
        newplates = []
        for plate_nr, plate in enumerate(plates):
            newplate = plate.copy()
            # a list to check for used well numbers, to prevent user from
            # setting the same well-number twice on a plate when re-ordering
            _used_wells = []
            for w_nr in range(1, 9):
                w_nr = str(w_nr)
                nw = plate['well-number-%s' % w_nr]
                if nw in _used_wells:
                    msg = "Well number %s on plate %s" % (nw, plate_nr + 1)
                    raise DuplicateWellSelected(msg)
                _used_wells.append(nw)
                for c_nr in range(1, 5):
                    key = 'chip-%s_well-%s'
                    newplate[key % (c_nr, nw)] = plate[key % (c_nr, w_nr)]
            newplates.append(newplate)
        return newplates

    def remove_empty_plates(self, plates):
        """Remove all plates that don't have (meaningful) values.
        """
        newplates = []
        for plate in plates:
            values = [plate[x] for x in plate.keys()
                      if not x.startswith('well-number-')]
            if any(values):
                newplates.append(plate)
        return newplates

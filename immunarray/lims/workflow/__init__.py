import sys


def AfterTransitionEventHandler(instance, event):
    """ This event is executed after each transition and delegates further
    actions to 'after_x_transition_event' function if exists in the instance
    passed in, where 'x' is the id of the event's transition.
    If the passed in instance has not a function with the abovementioned
    signature, or if there is no transition for the state change (like the
    'creation' state) or the same transition has already been run for the
    the passed in instance during the current server request, then the
    function does nothing.
    :param instance: the instance that has been transitioned
    :type instance: ATContentType
    :param event: event that holds the transition performed
    :type event: IObjectEvent
    """
    if not event.transition:
        return
    try:
        portal_type = instance.portal_type.lower()
        wfmodule = _load_wf_module('{0}.events'.format(portal_type))
    except ImportError:
        return
    if not wfmodule:
        return
    key = 'after_{0}'.format(event.transition.id)
    after_event = getattr(wfmodule, key, False)
    if not after_event:
        return
    after_event(instance)


def _load_wf_module(modrelname):
    """Loads a python module based on the module relative name passed in.
    At first, tries to get the module from sys.modules. If not found there, the
    function tries to load it by using importlib. Returns None if no module
    found or importlib is unable to load it because of errors.
    Ex:
        _load_wf_module('sample.events')
    will try to load the module 'immunarray.lims.workflow.sample.events'
    :param modrelname: relative name of the module to be loaded
    :type modrelname: string
    :return: the module
    :rtype: module
    """
    rootmodname = __name__
    modulekey = '{0}.{1}'.format(rootmodname, modrelname)
    if modulekey in sys.modules:
        return sys.modules.get(modulekey, None)

    # Try to load the module recursively
    modname = None
    tokens = modrelname.split('.')
    for part in tokens:
        modname = '.'.join([modname, part]) if modname else part
        import importlib
        try:
            _mod = importlib.import_module('.' + modname, package=rootmodname)
        except ImportError:
            return None
        if not _mod:
            return None
    return sys.modules.get(modulekey, None)


def GuardHandler(instance, transition_id):
    """Generic workflow guard handler that returns true if the transition_id
    passed in can be performed to the instance passed in.
    This function is called automatically by a Script (Python) located at
    bika/lims/skins/guard_handler.py, which in turn is fired by Zope when an
    expression like "python:here.guard_handler('<transition_id>')" is set to
    any given guard (used by default in all bika's DC Workflow guards).
    Walks through immunarray.lims.workflow.<obj_type>.guards and looks for a function
    that matches with 'guard_<transition_id>'. If found, calls the function and
    returns its value (true or false). If not found, returns True by default.
    Example:
    If exists an action with id 'publish' for a given workflow, and there is a
    guard expression set for this transition as follows:
        python: here.guard_handler('publish')
    When Zope fires this expression to evaluate if the transition 'publish' can
    be performed to a given Analysis Request, this function will try to find
    the following function:
        immunarray.lims.workflow.analysisrequest.guards.guard_publish(obj)
        (where obj is the Analysis Request object)
    If found, this function will be called and the result returned. Otherwise,
    will return True.
    :param instance: the object for which the transition_id has to be evaluated
    :param transition_id: the id of the transition
    :type instance: ATContentType
    :type transition_id: string
    :return: true if the transition can be performed to the passed in instance
    :rtype: bool
    """
    clazzname = instance.portal_type

    # Inspect if immunarray.lims.workflow.<clazzname>.<guards> module exists
    wfmodule = _load_wf_module('{0}.guards'.format(clazzname.lower()))
    if not wfmodule:
        return True

    # Inspect if guard_<transition_id> function exists in the above module
    key = 'guard_{0}'.format(transition_id)
    guard = getattr(wfmodule, key, False)
    if not guard:
        return True

    # pack = '{0}.guards'.format(clazzname.lower())
    # logger.info("{0}.{1}".format(pack, key))
    return guard(instance)

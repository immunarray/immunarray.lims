import json

from plone.app.z3cform.inline_validation import InlineValidationView as _ivv


class InlineValidationView(_ivv):
    """InlineValidationView's __call__ is ovrridden here because required-date 
    fields are too quick to flag a 'Required input is missing.' error.

    I'm removing all instances of 'Required input is missing', since it's also
    irritating when walking around a form and intentionally delaying data
    entry on some fields.

    Inline-validation still works for real values.
    """

    def __call__(self, fname=None, fset=None):
        json_value = super(InlineValidationView, self).__call__(fname, fset)
        value = json.loads(json_value)
        if 'input is missing' in value.get('errmsg', ''):
            del(value['errmsg'])
        return json.dumps(value)

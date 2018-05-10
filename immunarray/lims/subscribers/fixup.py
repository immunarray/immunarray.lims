#
# run: bin/client1 -O Plone run path/to/fix.py

import transaction

from AccessControl.SecurityManagement import newSecurityManager
from immunarray.lims.interfaces.aliquot import IAliquot
from immunarray.lims.interfaces.ichip import IiChip
from immunarray.lims.interfaces.sample import ISample
from plone.app.contenttypes import permissions

# login
user_name_or_id = 'jpitts'
user = app.Plone.acl_users.getUser(user_name_or_id)
newSecurityManager(None, user.__of__(app.Plone.acl_users))

# allow aliquots to have images inserted by the clock
# this is allowed for new site in subscribers/aliquot.py
for brain in app.Plone.portal_catalog(
        object_provides=[IAliquot.__identifier__,
                         ISample.__identifier__,
                         IiChip.__identifier__]):
    instance = brain.getObject()
    instance.manage_permission(
        permissions.AddImage, ['LabManager', 'LabClerk'], 0)
    print("%s addImage ['LabManager', 'LabClerk']" % instance)

transaction.commit()

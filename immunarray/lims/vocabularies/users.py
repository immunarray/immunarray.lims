# -*- coding: utf-8 -*-
from plone.api.portal import get_tool
from zope.interface import implementer
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary


@implementer(IContextSourceBinder)
class Users(object):
    """ Present a vocabulary containing users in the specified list of roles
    """

    def __init__(self, roles=None):
        if roles:
            if isinstance(roles, (tuple, list)):
                self.roles = roles
            else:
                self.roles = [roles]
        self.roles = []

    def __call__(self, context):
        mtool = get_tool('portal_membership')
        users = mtool.searchForMembers(roles=self.roles)
        items = [(item.getProperty('fullname'), item.getId()) for item in users]
        items.sort(lambda x, y: cmp(x[0].lower(), y[0].lower()))
        items = [SimpleTerm(i[1], i[1], i[0]) for i in items]
        return SimpleVocabulary(items)


UserVocabulary = Users()
LabUsersUserVocabulary = Users(
    ['LabManager', 'LabClerk', 'RandDLabClerk', 'RandDLabManager'])
ClinicalUserVocabulary = Users(
    ['LabManager', 'LabClerk', 'RandDLabClerk', 'RandDLabManager'])

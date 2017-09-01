# -*- coding: utf-8 -*-
from plone.app.content.browser.contents import FolderContentsView


class Samples(FolderContentsView):
    @property
    def ignored_columns(self):
        return super(Samples, self).ignored_columns


class Sites(FolderContentsView):
    @property
    def ignored_columns(self):
        return super(Sites, self).ignored_columns


class Materials(FolderContentsView):
    @property
    def ignored_columns(self):
        return super(Materials, self).ignored_columns


class Solutions(FolderContentsView):
    @property
    def ignored_columns(self):
        return super(Solutions, self).ignored_columns


class iChipLots(FolderContentsView):
    @property
    def ignored_columns(self):
        return super(iChipLots, self).ignored_columns


class TestRuns(FolderContentsView):
    @property
    def ignored_columns(self):
        return super(TestRuns, self).ignored_columns


class NonConformanceEvents(FolderContentsView):
    @property
    def ignored_columns(self):
        return super(NonConformanceEvents, self).ignored_columns


class Inventory(FolderContentsView):
    @property
    def ignored_columns(self):
        return super(Inventory, self).ignored_columns


class Patients(FolderContentsView):
    @property
    def ignored_columns(self):
        return super(Patients, self).ignored_columns


class Providers(FolderContentsView):
    @property
    def ignored_columns(self):
        return super(Providers, self).ignored_columns

class iChipAssays(FolderContentsView):
    @property
    def ignored_columns(self):
        return super(iChipAssays, self).ignored_columns

from plone.app.content.browser.contents import FolderContentsView


class View(FolderContentsView):
    @property
    def ignored_columns(self):
        return super(View, self).ignored_columns()

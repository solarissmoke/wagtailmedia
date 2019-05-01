from __future__ import absolute_import, unicode_literals

from wagtailmedia.widgets import AdminMediaChooser

from wagtail.admin.edit_handlers import BaseChooserPanel


class MediaChooserPanel(BaseChooserPanel):
    object_type_name = 'media'

    def widget_overrides(self):
        return {self.field_name: AdminMediaChooser}

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from django.utils.translation import ugettext as _

@plugin_pool.register_plugin
class TaccsiteImageGalleryPlugin(CMSPluginBase):
    """
    Components > "Image Gallery" Plugin
    https://confluence.tacc.utexas.edu/x/LIAjCQ
    """
    module = 'TACC Site'
    name = _('Image Gallery')
    render_template = 'image_gallery.html'

    cache = False
    text_enabled = False
    allow_children = True
    child_classes = [
        'PicturePlugin',
        'Bootstrap4PicturePlugin',
        'ImagePlugin',
    ]

    # Render

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)

        context.update({
            'child_classes': child_classes
        })

        return context

    @classmethod
    def get_empty_change_form_text(cls, obj=None):
        return _('To add an image, nest an "Image" or "Picture / Image" plugin inside this plugin.')

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from django.utils.translation import gettext as _

from .constants import TEXT_FOR_NESTED_PLUGIN_CONTENT_ADD

@plugin_pool.register_plugin
class TaccsiteImageGalleryPlugin(CMSPluginBase):
    """
    Components > "Image Gallery" Plugin
    https://confluence.tacc.utexas.edu/x/LIAjCQ
    """
    module = 'TACC Site'
    name = _('Image Gallery')
    render_template = 'image_gallery.html'

    cache = True
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
        request = context['request']

        assets_loaded = request.session.get('assets_loaded', False)
        if not assets_loaded:
            request.session['assets_loaded'] = True
            assets_loaded = True

        context.update({
            'assets_loaded': request.session['assets_loaded']
        })
        return context

    @classmethod
    def get_empty_change_form_text(cls, obj=None):
        return _(TEXT_FOR_NESTED_PLUGIN_CONTENT_ADD.format(
            element='an image',
            plugin_name='Image'
        ))

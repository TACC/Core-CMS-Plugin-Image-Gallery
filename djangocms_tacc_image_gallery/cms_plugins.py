from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from django.utils.translation import gettext as _

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

    fieldsets = [
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'attributes',
            )
        }),
    ]

    # Render

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        request = context['request']

        assets_loaded = request.session.get('assets_loaded', False)
        if not assets_loaded:
            request.session['assets_loaded'] = True

        classes = concat_classnames([
            's-image-gallery',
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes

        return context

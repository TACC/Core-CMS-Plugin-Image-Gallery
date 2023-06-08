from cms.models.pluginmodel import CMSPlugin

from djangocms_attributes_field import fields

class TaccsiteImageGallery(CMSPlugin):
    """
    Components > "Image Gallery" Model
    """
    attributes = fields.AttributesField()

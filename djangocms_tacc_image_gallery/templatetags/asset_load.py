from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def are_assets_loaded(context):
    return context.get('are_assets_loaded')

@register.simple_tag(takes_context=True)
def set_assets_loaded(context, value):
    context['set_assets_loaded'] = value

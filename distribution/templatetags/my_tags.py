from django import template

from config.settings import MEDIA_ROOT, MEDIA_URL


register = template.Library()

@register.filter
def mediapath(value: str) -> str:
    if value:
        return f'{MEDIA_URL}+{value}'
    else:
        return '#'

@register.simple_tag
def mediapath(value: str) -> str:
    if value:
        return f'{MEDIA_ROOT}+{value}'
    else:
        return '#'

from django import template

from config.settings import MEDIA_ROOT, MEDIA_URL
from send.models import Send

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

@register.simple_tag
def count_acive(object_list: list[Send]) -> int:
    if object_list:
        count = 0
        for obj in object_list:
            if obj.params.status.name == 'Запущено':
                count += 1
        return count
    else:
        return '#'

@register.simple_tag
def unique_client(object_list: list[Send]) -> int:
    if object_list:
        clients = set()
        for obj in object_list:
            clients.add(obj.client.email)
        return len(clients)
    else:
        return '#'
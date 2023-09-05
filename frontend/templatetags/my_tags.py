from django import template

from config.settings import MEDIA_ROOT, MEDIA_URL
from mailing.models import Mailing

register = template.Library()

@register.filter
def mediapath(value: str) -> str:
    if value:
        return f'{MEDIA_URL}{value}'
    else:
        return '#'

@register.simple_tag
def mediapath(value: str) -> str:
    if value:
        return f'{MEDIA_ROOT}{value}'
    else:
        return '#'

@register.simple_tag
def count_acive(object_list: list[Mailing]) -> int:
    if object_list:
        count = 0
        for obj in object_list:
            if obj.send.status.name == 'Запущена':
                count += 1
        return count
    else:
        return '#'

@register.simple_tag
def unique_client(object_list: list[Mailing]) -> int:
    if object_list:
        mailing_list = set()
        for obj in object_list:
            mailing_list.add(obj.client.email)
        return len(mailing_list)
    else:
        return '#'

@register.simple_tag
def run_mailer(pk):
    all_senders = Mailing.objects.filter(user=pk, send__pk=[1, 2])
                                         # send.status=['Создана', 'Запущена', 'Завершена'])


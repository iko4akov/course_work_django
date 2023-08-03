from django.core.management import BaseCommand

from utils.fills.fill import fill
from status.models import Status
from period.models import Period
from message.models import Message
from client.models import Client
from send.models import Send


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        fill([
            {'pk': 1, 'name': 'Создана'},
            {'pk': 2, 'name': 'Запущена'},
            {'pk': 3, 'name': 'Завершена'},
        ], Status)

        fill([
            {'pk': 1, 'name': 'День'},
            {'pk': 2, 'name': 'Неделя'},
            {'pk': 3, 'name': 'Месяц'},
        ], Period)

        fill([
            {'pk': 1, 'first_name': 'День', 'email': '111@111.com', 'comment': '111111'},
            {'pk': 2, 'first_name': 'Неделя', 'email': '222@222.com', 'comment': '222222'},
            {'pk': 3, 'first_name': 'Месяц', 'email': '333@333.com', 'comment': '333333'},
        ], Client)

        fill([
            {'pk': 1, 'theme': 'Внимание', 'message': '111111111111'},
            {'pk': 2, 'theme': 'Поздравление', 'message': '22222222222'},
            {'pk': 3, 'theme': 'Важная информация', 'message': '333333333333'},
        ], Message)

        fill([
            {'pk': 1, 'status': Status.objects.get(pk=3), 'message': Message.objects.get(pk=2), 'period': Period.objects.get(pk=2), 'time': "17:10:50"},
            {'pk': 2, 'status': Status.objects.get(pk=2), 'message': Message.objects.get(pk=1), 'period': Period.objects.get(pk=1), 'time': "17:10:50"},
            {'pk': 3, 'status': Status.objects.get(pk=1), 'message': Message.objects.get(pk=3), 'period': Period.objects.get(pk=3), 'time': "17:10:50"},
        ], Send)

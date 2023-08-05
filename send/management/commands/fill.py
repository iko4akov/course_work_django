from django.core.management import BaseCommand

from services.fills.fill import fill
from status.models import Status
from period.models import Period
from message.models import Message
from client.models import Client
from send.models import Send


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        fill([
            {'name': 'Создана'},
            {'name': 'Запущена'},
            {'name': 'Завершена'},
        ], Status)

        fill([
            {'name': 'День'},
            {'name': 'Неделя'},
            {'name': 'Месяц'},
        ], Period)

        fill([
            {'first_name': 'Перваков', 'second_name': 'Первый', 'third_name': 'Первович', 'email': '111@111.com', 'comment': '111111'},
            {'first_name': 'Второков', 'second_name': 'Второй', 'third_name': 'Вторович', 'email': '222@222.com', 'comment': '222222'},
            {'first_name': 'Третьяков', 'second_name': 'Третий', 'third_name': 'Третьевич', 'email': '333@333.com', 'comment': '333333'},
        ], Client)

        fill([
            {'theme': 'Внимание', 'message': '111111111111'},
            {'theme': 'Поздравление', 'message': '22222222222'},
            {'theme': 'Важная информация', 'message': '333333333333'},
        ], Message)

        fill([
            {'status': Status.objects.get(pk=3), 'message': Message.objects.get(pk=2),
             'period': Period.objects.get(pk=2), 'time': "17:10:50", 'client': Client.objects.get(pk=1)},
            {'status': Status.objects.get(pk=2), 'message': Message.objects.get(pk=1),
             'period': Period.objects.get(pk=1), 'time': "17:10:50", 'client': Client.objects.get(pk=2)},
            {'status': Status.objects.get(pk=1), 'message': Message.objects.get(pk=3),
             'period': Period.objects.get(pk=3), 'time': "17:10:50", 'client': Client.objects.get(pk=3)},
        ], Send)

from django.core.management import BaseCommand

from services.fills.fill import fill
from status.models import Status
from period.models import Period
from message.models import Message
from client.models import Client
from send.models import Send
from user.models import User


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
            {'first_name': 'Перваков', 'second_name': 'Первый', 'third_name': 'Первович', 'email': '111@111.com',
             'user': User.objects.get(pk=1), 'comment': '111111'},
            {'first_name': 'Второков', 'second_name': 'Второй', 'third_name': 'Вторович', 'email': '222@222.com',
             'user': User.objects.get(pk=1), 'comment': '222222'},
            {'first_name': 'Третьяков', 'second_name': 'Третий', 'third_name': 'Третьевич', 'email': '333@333.com',
             'user': User.objects.get(pk=1), 'comment': '333333'},
        ], Client)

        fill([
            {'theme': 'Внимание', 'message': 'Опасность взлома', 'user': User.objects.get(pk=1),},
            {'theme': 'Поздравление', 'message': 'С Днем рождения! ', 'user': User.objects.get(pk=1),},
            {'theme': 'Важная информация', 'message': 'Премия будет такого то числа', 'user': User.objects.get(pk=1),},
        ], Message)

        fill([
            {'status': Status.objects.get(pk=3), 'message': Message.objects.get(pk=2),
             'period': Period.objects.get(pk=2), 'time': "17:10:50", 'user': User.objects.get(pk=1)},
            {'status': Status.objects.get(pk=2), 'message': Message.objects.get(pk=1),
             'period': Period.objects.get(pk=1), 'time': "17:10:50", 'user': User.objects.get(pk=1)},
            {'status': Status.objects.get(pk=1), 'message': Message.objects.get(pk=3),
             'period': Period.objects.get(pk=3), 'time': "17:10:50", 'user': User.objects.get(pk=1)},
        ], Send)

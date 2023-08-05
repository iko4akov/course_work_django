from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from send.models import Send


def send_email_(send_item: Send):
    print(send_item.message.theme)
    print(send_item.message.message)
    print(EMAIL_HOST_USER)
    print(send_item.client.email)
    send_mail(
        send_item.message.theme,
        send_item.message.message,
        EMAIL_HOST_USER,
        [f'{send_item.client.email}'],
    )

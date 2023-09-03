from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from send.models import Send


# def send_email_(send_item: Send):
#     send_mail(
#         send_item.message.theme,
#         send_item.message.message,
#         EMAIL_HOST_USER,
#         [f'{send_item.client.email}'],
#     )
def send_email(email, verify_number=None, info='Для подтверждения почты введите в приложении'):
    send_mail(
        'Verification email',
        f'{info} {verify_number}',
        from_email=EMAIL_HOST_USER,
        recipient_list=[email]
    )

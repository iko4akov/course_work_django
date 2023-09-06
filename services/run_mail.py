from django.core.exceptions import ValidationError
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from logs.models import Logs
from mailing.models import Mailing


def run_mailer(period):
    mails = Mailing.objects.all()
    for mail in mails:
        email = mail.user.email
        message = mail.send.message.message
        theme = mail.send.message.theme
        get_period = mail.send.period.name
        if get_period == period:
            try:
                send_mail(theme, message, from_email=EMAIL_HOST_USER, recipient_list=[email])

            except ValidationError as e:
                log = Logs(send=mail.send, respounse=f"Ошибка валидации: {e}")
                log.save()

            except Exception as e:
                log = Logs(send=mail.send, respounse=f"Ошибка при отправке письма: {str(e)}")
                log.save()

            else:
                log = Logs(send=mail.send, respounse=f"Письмо успешно отправлено")
                log.save()
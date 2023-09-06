from django.core.exceptions import ValidationError
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from logs.models import Logs
from mailing.models import Mailing


def run_per_month():
    mails = Mailing.objects.all()
    for mail in mails:
        email = mail.user.email
        message = mail.send.message.message
        theme = mail.send.message.theme
        period = mail.send.period.name
        if period == 'Месяц':
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

def run_per_day():
    mails = Mailing.objects.all()
    for mail in mails:
        email = mail.user.email
        message = mail.send.message.message
        theme = mail.send.message.theme
        period = mail.send.period.name
        if period == 'День':

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

def run_per_week():
    mails = Mailing.objects.all()
    for mail in mails:
        email = mail.user.email
        message = mail.send.message.message
        theme = mail.send.message.theme
        period = mail.send.period.name
        if period == 'Неделя':
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

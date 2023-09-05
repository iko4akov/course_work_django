from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER

def send_email(email, verify_number=None, info='Для подтверждения почты введите в приложении'):
    send_mail(
        'Verification email',
        f'{info} {verify_number}',
        from_email=EMAIL_HOST_USER,
        recipient_list=[email]
    )

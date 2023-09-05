from django.core.management import BaseCommand

from services.run_mailer import run_mailer

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        run_mailer()

from django.contrib import admin

from mailing.models import Mailing


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('user', 'client', 'send')
    list_filter = ('user', 'client', 'send')
    search_fields = ('user', 'client', 'send')

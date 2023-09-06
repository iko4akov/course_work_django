from django.contrib import admin

from mailing.models import Mailing


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Mailing._meta.fields]
    search_fields = [field.name for field in Mailing._meta.fields]
    list_filter = [field.name for field in Mailing._meta.fields]

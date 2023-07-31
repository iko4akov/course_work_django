from django.contrib import admin

from logs.models import Logs


@admin.register(Logs)
class LogsAdmin(admin.ModelAdmin):
    list_display = ('try_last',)

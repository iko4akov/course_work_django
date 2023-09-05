from django.contrib import admin

from logs.models import Logs


@admin.register(Logs)
class LogsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Logs._meta.fields]
    list_filter = [field.name for field in Logs._meta.fields]
    search_fields = [field.name for field in Logs._meta.fields]

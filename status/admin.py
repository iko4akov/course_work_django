from django.contrib import admin

from status.models import Status


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)
    list_filter = ('name',)
    search_fields = ('name',)

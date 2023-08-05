from django.contrib import admin

from send.models import Send


@admin.register(Send)
class SendAdmin(admin.ModelAdmin):
    list_display = ('client', 'status', 'period', 'time')
    list_filter = ('client', 'status', 'period', 'time')
    search_fields = ('client', 'status', 'period', 'time')

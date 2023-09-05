from django.contrib import admin

from send.models import Send


@admin.register(Send)
class SendAdmin(admin.ModelAdmin):
    list_display = ('status', 'period', 'time', 'message', 'user')
    list_filter = ('status', 'period', 'time', 'message', 'user')
    search_fields = ('status', 'period', 'time', 'message', 'user')

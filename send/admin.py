from django.contrib import admin

from send.models import Send


@admin.register(Send)
class SendAdmin(admin.ModelAdmin):
    list_display = ('params', 'client')
    list_filter = ('params', 'client')
    search_fields = ('params', 'client')

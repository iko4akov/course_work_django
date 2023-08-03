from django.contrib import admin

from send.models import Send


@admin.register(Send)
class SendAdmin(admin.ModelAdmin):
    list_display = ('client',)
    list_filter = ('client',)
    search_fields = ('client',)

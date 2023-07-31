from django.contrib import admin

from message.models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'theme', 'message',)
    search_fields = ('message', 'theme', )

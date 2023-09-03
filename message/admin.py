from django.contrib import admin

from message.models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('theme', 'message', 'user')
    search_fields = ('message', 'theme', )

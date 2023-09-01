from django.contrib import admin

from client.apps import ClientConfig
from client.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'second_name', 'third_name', 'email', 'user')
    list_filter = ('email', 'first_name',)
    search_fields = ('comment', 'email', 'first_name', )

from django.contrib import admin
from distribution.models import Client, Status, Period, Distription, Message, Logs


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name',)

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Period)
class PeriodAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('theme',)

@admin.register(Distription)
class DistriptionAdmin(admin.ModelAdmin):
    list_display = ('time',)

@admin.register(Logs)
class LogsAdmin(admin.ModelAdmin):
    list_display = ('try_last',)

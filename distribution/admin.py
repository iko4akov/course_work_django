from django.contrib import admin
from distribution.models import Client, Status, Period, Distribution, Message, Logs, DistributClien


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'second_name', 'third_name', 'email')
    list_filter = ('email', 'first_name')
    search_fields = ('comment', )

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)
    list_filter = ('name',)
    search_fields = ('name',)

@admin.register(Period)
class PeriodAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', )
    list_filter = ('name', )
    search_fields = ('name', )

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'theme', 'message',)
    search_fields = ('message', 'theme', )

@admin.register(Distribution)
class DistributionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'time', 'period', 'status')
    list_filter = ('time', 'period', 'status')
    search_fields = ('time', 'period', 'status')

@admin.register(Logs)
class LogsAdmin(admin.ModelAdmin):
    list_display = ('try_last',)


@admin.register(DistributClien)
class DistributClienAdmin(admin.ModelAdmin):
    list_display = ('distribution', 'client', )
    list_filter = ('distribution', 'client', )
    search_fields = ('distribution', 'client', )

from django.contrib import admin

from period.models import Period


@admin.register(Period)
class PeriodAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)
    list_filter = ('name',)
    search_fields = ('name',)

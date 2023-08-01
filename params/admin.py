from django.contrib import admin
from params.models import Params


@admin.register(Params)
class ParamsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'time', 'period', 'status')
    list_filter = ('time', 'period', 'status')
    search_fields = ('time', 'period', 'status')

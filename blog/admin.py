from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Blog._meta.fields]
    search_fields = [field.name for field in Blog._meta.fields]
    list_filter = [field.name for field in Blog._meta.fields]

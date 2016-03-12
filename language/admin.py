from django.contrib import admin

from .models import Language


@admin.register(Language)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['id', 'language']

from django.contrib import admin

from .models import StudioModel

# Register your models here.


@admin.register(StudioModel)
class StudioAdmin(admin.ModelAdmin):
    search_fields = ["name"]
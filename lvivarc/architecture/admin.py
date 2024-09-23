from django.contrib import admin
from .models import ArchitectureGroup

# Register your models here.
@admin.register(ArchitectureGroup)
class ArchitectureGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'slug')
    prepopulated_fields = {'slug' : ('title',)}
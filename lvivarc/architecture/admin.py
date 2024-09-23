from django.contrib import admin
from .models import ArchitectureGroup, ArchitectureObject

# Register your models here.
@admin.register(ArchitectureGroup)
class ArchitectureGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'slug')
    prepopulated_fields = {'slug' : ('title',)}

@admin.register(ArchitectureObject)
class ArchitecureObjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'address')
    search_fields = ('title',   )
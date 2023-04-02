from django.contrib import admin
from . models import Task

# Register your models here.

@admin.register(Task)
class TaskModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'owner', 'label', 'description', 'begin', 'end', 'priority', 'done']
from django.contrib import admin
from .models import Task

# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list = ('title', 'assigned_to', 'status', 'priority', 'due_date', 'created_at')
    search = ('title', 'desc')
    filetr = ('status', 'priority', 'due_date')

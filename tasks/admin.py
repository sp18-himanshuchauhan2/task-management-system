from django.contrib import admin
from .models import Task, Status, Priority

# Register your models here.

admin.site.register(Task)
admin.site.register(Status)
admin.site.register(Priority)

# @admin.register(Task)
# class TaskAdmin(admin.ModelAdmin):
#     list = ('title', 'assigned_to', 'status', 'priority', 'due_date', 'created_at')
#     search = ('title', 'desc')
#     filetr = ('status', 'priority', 'due_date')

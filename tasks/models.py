from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Status(models.Model):
    st = models.CharField(max_length=30)

    def __str__(self):
        return self.st


class Priority(models.Model):
    pr = models.CharField(max_length=30)

    def __str__(self):
        return self.pr

class Task(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(blank=True)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    priority = models.ForeignKey(Priority, on_delete=models.SET_NULL, null=True)
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



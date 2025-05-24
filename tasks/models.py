from django.db import models

# Create your models here.
from users.models import User
from statuses.models import Status
from labels.models import Label

class Task(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    labels = models.ManyToManyField(Label, related_name='tasks')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tasks')
    executor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='executed_tasks')
    created_at = models.DateTimeField(auto_now_add=True)
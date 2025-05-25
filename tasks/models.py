from django.db import models
from users.models import User
from statuses.models import Status
from labels.models import Label


class Task(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    executor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='executed_tasks')

    creator = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='created_tasks'
    )
    labels = models.ManyToManyField(Label, related_name='tasks')

    created_at = models.DateTimeField(auto_now_add=True)
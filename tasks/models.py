# tasks/models.py

from django.db import models
from users.models import User
from statuses.models import Status
from labels.models import Label
from django.utils.translation import gettext_lazy as _


class Task(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        null=True,
        verbose_name=_('Status')
    )
    executor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=True,
        related_name='executed_tasks',
        verbose_name=_('Executor')
    )
    creator = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='created_tasks',
        verbose_name=_('Author')
    )
    labels = models.ManyToManyField(
        Label,
        related_name='tasks',
        blank=True,
        verbose_name=_('Labels')
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
# tasks/models.py

from django.db import models
from users.models import User
from statuses.models import Status
from labels.models import Label
from django.utils.translation import gettext_lazy as _


class Task(models.Model):
    name = models.CharField(
        _("Имя"),
        max_length=255,
        unique=True
    )
    description = models.TextField(_('Описание'))
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        null=True,
        verbose_name=_('Статус')
    )
    executor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='executed_tasks',
        verbose_name=_('Исполнитель')
    )
    creator = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='created_tasks', null=True, blank=True,
        verbose_name=_('Автор')
    )
    labels = models.ManyToManyField(
        Label,
        related_name='tasks',
        blank=True,
        verbose_name=_('Метки')
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.db import models
from django.core.exceptions import ObjectDoesNotExist

from tasks.models import Task


class ProtectedDeleteMixin:
    protected_message = "Этот объект нельзя удалить, так как он используется"
    protected_url = reverse_lazy("tasks:index")

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()

        # Проверка ManyToMany (для меток)
        if hasattr(obj, 'tasks') and obj.tasks.exists():
            messages.error(request, self.protected_message)
            return redirect(self.protected_url)

        # Проверка ForeignKey (для статусов, пользователей)
        if hasattr(self, 'related_filter'):
            filter_kwargs = self.related_filter()
            if Task.objects.filter(**filter_kwargs).exists():
                messages.error(request, self.protected_message)
                return redirect(self.protected_url)

        try:
            return super().delete(request, *args, **kwargs)
        except ProtectedError:
            messages.error(request, self.protected_message)
            return redirect(self.protected_url)

class OnlyAuthorMixin(UserPassesTestMixin):
    permission_denied_message = "Вы не можете редактировать или удалять чужие задачи"
    permission_denied_url = reverse_lazy('tasks:index')

    def test_func(self):
        obj = self.get_object()
        if hasattr(obj, 'creator'):
            return obj.creator == self.request.user
        return False

    def handle_no_permission(self):
        messages.error(self.request, self.permission_denied_message)
        return redirect(self.permission_denied_url)
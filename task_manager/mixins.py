from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from django.db.models import ProtectedError
from django.db import IntegrityError
from django.utils.translation import gettext_lazy as _

class ProtectedDeleteMixin:
    """
    Миксин для защиты от удаления объекта, если он используется.
    Должен стоять первым в списке родителей!
    """
    protected_message = _("Невозможно удалить объект, потому что он используется")
    protected_url = reverse_lazy('users:index')

    def form_valid(self, form):
        obj = self.get_object()


        if hasattr(obj, 'tasks') and obj.tasks.exists():
            messages.error(self.request, self.protected_message)
            return redirect(self.protected_url)


        if hasattr(self, 'related_filter'):
            from tasks.models import Task
            filter_kwargs = self.related_filter()
            if Task.objects.filter(**filter_kwargs).exists():
                messages.error(self.request, self.protected_message)
                return redirect(self.protected_url)

        try:
            return super().form_valid(form)
        except ProtectedError:
            messages.error(self.request, self.protected_message)
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
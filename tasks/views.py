# tasks/views.py
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView, DetailView
)
from django_filters.views import FilterView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from task_manager.mixins import ProtectedDeleteMixin, OnlyAuthorMixin
from .models import Task
from .forms import TaskForm
from .filters import TaskFilter


TASKS_INDEX_URL = 'tasks:index'


class TaskListView(LoginRequiredMixin, FilterView):
    model = Task
    filterset_class = TaskFilter
    template_name = 'tasks/index.html'
    context_object_name = 'tasks'
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset
        return context


class TaskCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/create.html'
    success_url = reverse_lazy(TASKS_INDEX_URL)
    success_message = _("Задача успешно создана")

    extra_context = {
        'title': _('Создать задачу'),
        'button_name': _('Создать')
    }

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, OnlyAuthorMixin, SuccessMessageMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/update.html'
    success_url = reverse_lazy(TASKS_INDEX_URL)
    success_message = _("Задача успешно обновлена")

    extra_context = {
        'title': _('Редактировать задачу'),
        'button_name': _('Обновить')
    }


class TaskDetailView(LoginRequiredMixin, OnlyAuthorMixin, DetailView):
    model = Task
    template_name = 'tasks/detail.html'
    context_object_name = 'task'


class TaskDeleteView(OnlyAuthorMixin, ProtectedDeleteMixin, DeleteView):
    model = Task
    template_name = 'tasks/delete.html'
    success_url = reverse_lazy(TASKS_INDEX_URL)
    protected_url = reverse_lazy(TASKS_INDEX_URL)
    protected_message = _("Невозможно удалить задачу, потому что она используется")
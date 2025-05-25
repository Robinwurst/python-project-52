from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
from .forms import TaskForm
from django.shortcuts import redirect
from django.db import models
from task_manager.mixins import ProtectedDeleteMixin

TASKS_INDEX_URL = 'tasks:index'


class TaskListView(ListView):
    model = Task
    template_name = 'tasks/index.html'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/create.html'
    success_url = reverse_lazy(TASKS_INDEX_URL)

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/update.html'
    success_url = reverse_lazy(TASKS_INDEX_URL)


class TaskDeleteView(LoginRequiredMixin, ProtectedDeleteMixin, DeleteView):
    model = Task
    template_name = 'tasks/delete.html'
    success_url = reverse_lazy(TASKS_INDEX_URL)

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except models.ProtectedError as e:
            from django.contrib import messages
            messages.error(request, 'Невозможно удалить задачу, потому что она используется в других объектах.')
            return redirect(TASKS_INDEX_URL)
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
from .forms import TaskForm
from django.shortcuts import redirect
from django.db import models
from task_manager.mixins import ProtectedDeleteMixin
from django.views.generic import ListView
from users.models import User
from statuses.models import Status
from labels.models import Label
TASKS_INDEX_URL = 'tasks:index'


class TaskListView(ListView):
    model = Task
    template_name = 'tasks/index.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        queryset = super().get_queryset()
        status_id = self.request.GET.get('status')
        creator_id = self.request.GET.get('creator')
        executor_id = self.request.GET.get('executor')
        label_id = self.request.GET.get('label')

        if status_id:
            queryset = queryset.filter(status_id=status_id)
        if creator_id:
            queryset = queryset.filter(creator_id=creator_id)
        if executor_id:
            queryset = queryset.filter(executor_id=executor_id)
        if label_id:
            queryset = queryset.filter(labels=label_id)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['statuses'] = Status.objects.all()
        context['users'] = User.objects.all()
        context['labels'] = Label.objects.all()
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
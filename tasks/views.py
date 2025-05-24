from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskForm

class TaskListView(ListView):
    model = Task
    template_name = 'tasks/index.html'
    context_object_name = 'tasks'

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks')
    template_name = 'tasks/create.html'

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks')
    template_name = 'tasks/update.html'

class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks')
    template_name = 'tasks/delete.html'
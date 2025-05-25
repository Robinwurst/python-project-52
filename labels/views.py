from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Label
from .forms import LabelForm
from django.contrib.auth.mixins import LoginRequiredMixin
from task_manager.mixins import ProtectedDeleteMixin

class LabelListView(ListView):
    model = Label
    template_name = 'labels/index.html'

class LabelCreateView(LoginRequiredMixin, CreateView):
    model = Label
    form_class = LabelForm
    success_url = reverse_lazy('labels:index')
    template_name = 'labels/create.html'

class LabelUpdateView(LoginRequiredMixin, UpdateView):
    model = Label
    form_class = LabelForm
    success_url = reverse_lazy('labels:index')
    template_name = 'labels/update.html'

class LabelDeleteView(LoginRequiredMixin, ProtectedDeleteMixin, DeleteView):
    model = Label
    success_url = reverse_lazy('labels:index')
    template_name = 'labels/delete.html'
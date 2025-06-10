from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Label
from .forms import LabelForm
from django.contrib.auth.mixins import LoginRequiredMixin
from task_manager.mixins import ProtectedDeleteMixin, OnlyAuthorMixin


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

class LabelDeleteView(OnlyAuthorMixin, ProtectedDeleteMixin, DeleteView):
    model = Label
    template_name = 'labels/delete.html'
    success_url = reverse_lazy('labels:index')

    def delete(self, request, *args, **kwargs):
        label = self.get_object()


        if label.tasks.exists():
            from django.contrib import messages
            messages.error(request, "Метка используется в задачах и не может быть удалена")
            return redirect('labels:index')

        return super().delete(request, *args, **kwargs)
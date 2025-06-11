# Create your views here.
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from task_manager.mixins import ProtectedDeleteMixin
from .forms import LabelForm
from .models import Label


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

class LabelDeleteView(ProtectedDeleteMixin, DeleteView):
    model = Label
    template_name = 'labels/delete.html'
    success_url = reverse_lazy('labels:index')
    protected_message = "Невозможно удалить метку, потому что она используется"
    protected_url = reverse_lazy('labels:index')

    def delete(self, request, *args, **kwargs):
        label = self.get_object()
        if label.tasks.exists():
            messages.error(request, "Метка используется в задачах")
            return redirect(self.protected_url)
        return super().delete(request, *args, **kwargs)
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from task_manager.mixins import ProtectedDeleteMixin
from .models import Label
from .forms import LabelForm

LABEL_INDEX_URL = 'labels:index'
LABEL_TEMPLATE_PATH = 'labels/'

class LabelListView(LoginRequiredMixin, ListView):
    model = Label
    template_name = f'{LABEL_TEMPLATE_PATH}index.html'
    context_object_name = 'labels'
    ordering = ['id']
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().order_by('id')

class LabelCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Label
    form_class = LabelForm
    template_name = f'{LABEL_TEMPLATE_PATH}create.html'
    success_url = reverse_lazy(LABEL_INDEX_URL)
    success_message = _("Метка успешно создана")


class LabelUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Label
    form_class = LabelForm
    template_name = f'{LABEL_TEMPLATE_PATH}update.html'
    success_url = reverse_lazy(LABEL_INDEX_URL)
    success_message = _("Метка успешно изменена")


class LabelDeleteView(ProtectedDeleteMixin, SuccessMessageMixin, DeleteView):
    model = Label
    template_name = 'labels/delete.html'
    success_url = reverse_lazy('labels:index')
    protected_message = _("Невозможно удалить метку, потому что она используется в задачах")
    protected_url = reverse_lazy('labels:index')
    success_message = _("Метка успешно удалена")

    def delete(self, request, *args, **kwargs):
        label = self.get_object()
        if label.tasks.exists():
            messages.error(request, self.protected_message)
            return redirect(self.protected_url)
        return super().delete(request, *args, **kwargs)
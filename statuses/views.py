from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    ListView,
)
from .models import Status
from .forms import StatusCreateForm
from django.utils.translation import gettext_lazy as _
from task_manager.mixins import ProtectedDeleteMixin


class StatusListView(LoginRequiredMixin, ListView):
    model = Status
    template_name = 'statuses/index.html'
    context_object_name = 'statuses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = messages.get_messages(self.request)
        return context


class StatusCreateView(LoginRequiredMixin, CreateView):
    model = Status
    form_class = StatusCreateForm
    template_name = 'statuses/create.html'
    success_url = reverse_lazy('statuses')

    def form_valid(self, form):
        messages.success(self.request, _('Статус успешно создан'))
        return super().form_valid(form)


class StatusUpdateView(LoginRequiredMixin, UpdateView):
    model = Status
    form_class = StatusCreateForm
    template_name = 'statuses/update.html'
    success_url = reverse_lazy('statuses')

    def form_valid(self, form):
        messages.success(self.request, _('Статус успешно обновлен'))
        return super().form_valid(form)


class StatusDeleteView(LoginRequiredMixin, ProtectedDeleteMixin, DeleteView):
    model = Status
    template_name = 'statuses/delete.html'
    success_url = reverse_lazy('statuses')
    protected_message = _('Невозможно удалить статус, потому что он используется')
    protected_url = reverse_lazy('statuses')

    def form_valid(self, form):
        messages.success(self.request, _('Статус успешно удалён'))
        return super().form_valid(form)
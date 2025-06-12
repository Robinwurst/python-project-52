from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from task_manager.mixins import ProtectedDeleteMixin
from .models import Status
from .forms import StatusCreateForm

STATUS_INDEX_URL = 'statuses:index'
STATUS_TEMPLATE_PATH = 'statuses/'

class StatusListView(LoginRequiredMixin, ListView):
    model = Status
    template_name = f'{STATUS_TEMPLATE_PATH}index.html'
    context_object_name = 'statuses'
    ordering = ['id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = messages.get_messages(self.request)
        return context


class StatusCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Status
    form_class = StatusCreateForm
    template_name = f'{STATUS_TEMPLATE_PATH}create.html'
    success_url = reverse_lazy(STATUS_INDEX_URL)
    success_message = _("Статус успешно создан")
    extra_context = {
        'title': _('Создать статус'),
        'button_name': _('Создать')
    }


class StatusUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Status
    form_class = StatusCreateForm
    template_name = f'{STATUS_TEMPLATE_PATH}update.html'
    success_url = reverse_lazy(STATUS_INDEX_URL)
    success_message = _("Статус успешно обновлён")
    extra_context = {
        'title': _('Редактировать статус'),
        'button_name': _('Обновить')
    }


class StatusDeleteView(ProtectedDeleteMixin, DeleteView):
    model = Status
    template_name = 'statuses/delete.html'
    success_url = reverse_lazy('statuses:index')
    protected_message = _("Невозможно удалить статус, потому что он используется в задачах")
    protected_url = reverse_lazy('statuses:index')

    def related_filter(self):
        return {'status': self.get_object()}
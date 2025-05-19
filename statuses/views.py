from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    ListView,
)
from django.urls import reverse_lazy
from .models import Status
from .forms import StatusCreateForm
from django.contrib import messages

class StatusListView(ListView):
    model = Status
    template_name = 'statuses/index.html'
    context_object_name = 'statuses'

class StatusCreateView(CreateView):
    model = Status
    form_class = StatusCreateForm
    template_name = 'statuses/create.html'
    success_url = reverse_lazy('statuses')

    def post(self, request, *args, **kwargs):
        status = self.get_object()
        if hasattr(status, 'tasks') and status.tasks.exists():
            messages.error(request, 'Невозможно создать статус')
            return self.render_to_response(self.get_context_data())
        messages.success(request, 'Статус успешно создан')
        return super().post(request, *args, **kwargs)

class StatusUpdateView(UpdateView):
    model = Status
    form_class = StatusCreateForm
    template_name = 'statuses/update.html'
    success_url = reverse_lazy('statuses')

    def post(self, request, *args, **kwargs):
        status = self.get_object()
        if hasattr(status, 'tasks') and status.tasks.exists():
            messages.error(request, 'Невозможно обновить статус')
            return self.render_to_response(self.get_context_data())
        messages.success(request, 'Статус успешно обновленн')
        return super().post(request, *args, **kwargs)


class StatusDeleteView(DeleteView):
    model = Status
    template_name = 'statuses/delete.html'
    success_url = reverse_lazy('statuses')

    def post(self, request, *args, **kwargs):
        status = self.get_object()
        if hasattr(status, 'tasks') and status.tasks.exists():
            messages.error(request, 'Невозможно удалить статус, который используется в задачах')
            return self.render_to_response(self.get_context_data())
        messages.success(request, 'Статус успешно удалён')
        return super().post(request, *args, **kwargs)



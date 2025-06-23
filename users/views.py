from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    ListView,
)
from django.urls import reverse_lazy
from .models import User
from .forms import UserCreateForm, UserUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from task_manager.mixins import ProtectedDeleteMixin
from django.utils.translation import gettext_lazy as _

class UserListView(ListView):
    model = User
    template_name = 'users/index.html'
    context_object_name = 'users'
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().order_by('id')

class UserCreateView(CreateView):
    form_class = UserCreateForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('users:index')

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('users:index')

class UserDeleteView(LoginRequiredMixin, ProtectedDeleteMixin, SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users:index')
    protected_message = _("Невозможно удалить пользователя, потому что он используется в задачах")
    protected_url = reverse_lazy('users:index')
    success_message = "Пользователь успешно удален"
    def related_filter(self):
        return {'creator': self.get_object()}

class CustomLoginView(SuccessMessageMixin, LoginView):
    template_name = 'users/login.html'
    success_message = "Вы залогинены"
    next_page = reverse_lazy('home')

class CustomLogoutView(SuccessMessageMixin, LogoutView):
    next_page = reverse_lazy('home')
    success_message = "Вы разлогинены"

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, self.success_message)
        return super().dispatch(request, *args, **kwargs)
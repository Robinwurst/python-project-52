from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    ListView,
)
from django.contrib.auth.forms import UserChangeForm
from django.urls import reverse_lazy
from .models import User
from .forms import UserCreateForm, UserUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin

class UserListView(ListView):
    model = User
    template_name = 'users/index.html'
    context_object_name = 'users'

class UserCreateView(CreateView):
    form_class = UserCreateForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('users:index')

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('users:index')

class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users:index')
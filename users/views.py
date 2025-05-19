from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    ListView,
)
from django.urls import reverse_lazy
from .models import User
from .forms import UserCreateForm


class UserListView(ListView):
    model = User
    template_name = 'users/index.html'
    context_object_name = 'users'

class UserCreateView(CreateView):
    form_class = UserCreateForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('user_create')

class UserUpdateView(UpdateView):
    model = User
    form_class = UserCreateForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('users')

class UserDeleteView(DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users')
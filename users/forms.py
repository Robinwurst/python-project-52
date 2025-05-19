from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from .models import Status

class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class StatusCreateForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']
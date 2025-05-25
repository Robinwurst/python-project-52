from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.db import models

class ProtectedDeleteMixin:
    protected_message = 'Этот объект нельзя удалить, так как он используется'
    protected_url = reverse_lazy('home')

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except models.ProtectedError:
            from django.contrib import messages
            messages.error(request, self.protected_message)
            return redirect(self.protected_url)
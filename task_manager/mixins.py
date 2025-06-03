from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.db.models import ProtectedError

class ProtectedDeleteMixin:
    protected_message = 'Этот объект нельзя удалить, так как он используется'
    protected_url = reverse_lazy('home')

    def delete(self, request, *args, **kwargs):
        try:
            return super().delete(request, *args, **kwargs)
        except ProtectedError:
            from django.contrib import messages
            messages.error(request, self.protected_message)
            return redirect(self.protected_url)

    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
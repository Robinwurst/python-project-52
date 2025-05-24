from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


class ProtectedDeleteMixin:
    protected_message = None
    protected_url = None

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except Exception as e:
            if 'ProtectedError' in str(e):
                messages.error(request, self.protected_message)
                return HttpResponseRedirect(self.protected_url)
            raise
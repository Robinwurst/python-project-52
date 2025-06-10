import django_filters
from .models import Task
from users.models import User
from statuses.models import Status
from labels.models import Label


class TaskFilter(django_filters.FilterSet):
    status = django_filters.ModelChoiceFilter(queryset=Status.objects.all())
    creator = django_filters.ModelChoiceFilter(queryset=User.objects.all())
    executor = django_filters.ModelChoiceFilter(queryset=User.objects.all())
    labels = django_filters.ModelMultipleChoiceFilter(queryset=Label.objects.all())

    class Meta:
        model = Task
        fields = ['status', 'creator', 'executor', 'labels']
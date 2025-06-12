import django_filters
from django.utils.translation import gettext_lazy as _
from django.forms.widgets import CheckboxInput
from .models import Task
from statuses.models import Status
from users.models import User
from labels.models import Label


class TaskFilter(django_filters.FilterSet):
    status = django_filters.ModelChoiceFilter(
        queryset=Status.objects.all(),
        field_name='status',
        label=_('Статус'),
    )
    executor = django_filters.ModelChoiceFilter(
        queryset=User.objects.all(),
        field_name='executor',
        label=_('Исполнитель'),
    )
    creator = django_filters.ModelChoiceFilter(
        queryset=User.objects.all(),
        field_name='creator',
        label=_('Автор'),
    )
    labels = django_filters.ModelChoiceFilter(
        queryset=Label.objects.all(),
        field_name='labels',
        label=_('Метки'),
    )
    own_tasks = django_filters.BooleanFilter(
        widget=CheckboxInput,
        label=_('Только мои задачи'),
        method='filter_own_tasks',
    )

    class Meta:
        model = Task
        fields = ['status', 'executor', 'creator', 'labels', 'own_tasks']

    def filter_own_tasks(self, queryset, name, value):
        if value and self.request.user.is_authenticated:
            return queryset.filter(creator=self.request.user)
        return queryset
from django import forms

from users.models import User
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']

        def __init__(self, *args, **kwargs):
            super(TaskForm, self).__init__(*args, **kwargs)
            self.fields['executor'].queryset = User.objects.all()
            self.fields['executor'].label_from_instance = (
                lambda obj: f"{obj.first_name} {obj.last_name}"
            )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['executor'].required = False
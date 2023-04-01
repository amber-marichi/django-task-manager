from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.core.exceptions import ValidationError
from django_flatpickr.widgets import DateTimePickerInput

from hacelo.models import Task, TaskType


class TaskSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
    )


class WorkerSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
    )


class TaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        widget=DateTimePickerInput(attrs={"value": timezone.now()}),
    )

    class Meta:
        model = Task
        exclude = ["is_completed", "assignees",]

    def clean_deadline(self):
        deadline = self.cleaned_data["deadline"]
        if deadline < timezone.now():
            raise ValidationError("The date cannot be in the past")
        return deadline


class WorkerForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["position"].required = True

    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "position",
            "email",
        )


class TaskTypeForm(forms.ModelForm):

    class Meta:
        model = TaskType
        fields = "__all__"

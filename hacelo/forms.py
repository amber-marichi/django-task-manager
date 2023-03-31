from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from datetime import date

from hacelo.models import Task, TaskType


class TaskSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "search task by name..."}
        ),
    )


class WorkerSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
    )


class TaskForm(forms.ModelForm):
    # assignees = forms.ModelMultipleChoiceField(
    #     queryset=get_user_model().objects.all(),
    #     widget=forms.CheckboxSelectMultiple,
    #     required=False,
    # )
    today = date.today()
    deadline = forms.DateTimeField(
        widget=forms.widgets.DateTimeInput(
            attrs={"type": "date", "min": today, "value": today}
        ),
    )

    class Meta:
        model = Task
        exclude = ["is_completed",]


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

from django.test import TestCase
from django.utils import timezone
from datetime import timedelta

from hacelo.models import TaskType, Position
from hacelo.forms import WorkerForm, TaskForm


class FormsTestClass(TestCase):
    def test_worker_creation_form_valid_data(self) -> None:
        form_input = {
            "username": "testworker",
            "first_name": "TestFirstName",
            "last_name": "TestLastName",
            "email": "test@testers.org",
            "position": Position.objects.create(name="TestPosition",),
            "password1": "$eCr1tT4",
            "password2": "$eCr1tT4",
        }

        form = WorkerForm(data=form_input)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_input)

    def test_task_creation_form_valid_data(self) -> None:
        form_input = {
            "name": "TestTask",
            "description": "to test",
            "deadline": timezone.now() + timedelta(days=2),
            "priority": "1UR",
            "task_type": TaskType.objects.create(name="TestTaskType",),
        }
        form = TaskForm(data=form_input)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_input)

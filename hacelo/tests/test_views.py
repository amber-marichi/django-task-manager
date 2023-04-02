from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone

from hacelo.models import Position, Task, TaskType


class PrivateWorkerTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username="admin",
            password="13admin31",
        )
        self.client.force_login(self.user)

    def test_create_worker(self) -> None:
        pos = Position.objects.create(
            name="TestPosition",
        )

        form_input = {
            "username": "testworker",
            "first_name": "TestFirstName",
            "last_name": "TestLastName",
            "email": "test@testers.org",
            "position": pos.id,
            "password1": "$eCr1tT4",
            "password2": "$eCr1tT4",
        }

        self.client.post(reverse("hacelo:worker-create"), data=form_input)
        worker = get_user_model().objects.get(username=form_input["username"])

        self.assertEqual(worker.first_name, form_input["first_name"])
        self.assertEqual(worker.position.name, pos.name)
        self.assertEqual(worker.email, form_input["email"])


class PublicTaskTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.task = Task.objects.create(
            name="TestTask",
            description="to test",
            deadline=timezone.now(),
            is_completed=False,
            priority="1UR",
            task_type=TaskType.objects.create(name="TestTaskType",),
        )

    def test_login_required(self):
        response = self.client.get(
            reverse("hacelo:task-detail", kwargs={"pk": self.task.id})
        )

        self.assertNotEqual(response.status_code, 200)
        self.assertEqual(response.status_code, 302)

    def test_login_successful(self):
        user = get_user_model().objects.create_user(
            username="admin",
            password="13admin31",
        )
        self.client.force_login(user)

        response = self.client.get(
            reverse("hacelo:task-detail", kwargs={"pk": self.task.id})
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context["task"],
            self.task
        )


class WorkerSearchTest(TestCase):
    def test_serch_result_workers(self) -> None:
        get_user_model().objects.create(
            username="tesuser1",
            password="13admin3111",
        )
        get_user_model().objects.create(
            username="tesuser2",
            password="13admin3222",
        )
        get_user_model().objects.create(
            username="tesuser3",
            password="13admin3333",
        )

        response = self.client.get(
            reverse("hacelo:worker-list") + "?username=TeStUSe"
        )
        workers = get_user_model().objects.filter(
            username__icontains="TeStUSe"
        )

        self.assertQuerysetEqual(
            response.context["workers"],
            workers
        )

from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone

from hacelo.models import Position, Task, TaskType


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="13admin31",
        )
        self.client.force_login(self.admin_user)

        self.worker = get_user_model().objects.create(
            username="testworker",
            first_name="TestFirstName",
            last_name="TestLastName",
            password="$eCr1tT",
            position=Position.objects.create(name="TestPosition",),
        )

        self.task = Task.objects.create(
            name="TestTask",
            description="to test",
            deadline=timezone.now(),
            is_completed=False,
            priority="1UR",
            task_type=TaskType.objects.create(name="TestTaskType",),
        )
    
    def test_worker_list_position_field(self) -> None:
        url = reverse("admin:hacelo_worker_changelist")
        response = self.client.get(url)

        self.assertContains(response, self.worker.position.name)
    
    def test_worker_details_position_field(self) -> None:
        url = reverse("admin:hacelo_worker_change", args=[self.worker.id])
        response = self.client.get(url)

        self.assertContains(response, self.worker.position.name)
    
    def test_worker_create_custom_fields_present(self) -> None:
        url = reverse("admin:hacelo_worker_add")
        response = self.client.get(url)

        self.assertContains(response, "first_name")
        self.assertContains(response, "last_name")
        self.assertContains(response, "email")
        self.assertContains(response, "position")
    
    def test_task_list_custom_fields(self) -> None:
        url = reverse("admin:hacelo_task_changelist")
        response = self.client.get(url)

        self.assertContains(response, self.task.name)
        self.assertContains(response, self.task.task_type.name)
        self.assertContains(response, "priority")
        self.assertContains(response, "is_completed")
        self.assertContains(response, "deadline")

    def test_task_details_custom_fields(self) -> None:
        url = reverse("admin:hacelo_task_change", args=[self.task.id])
        response = self.client.get(url)

        self.assertContains(response, self.task.name)
        self.assertContains(response, self.task.task_type.name)
        self.assertContains(response, "priority")
        self.assertContains(response, "is_completed")
        self.assertContains(response, "deadline")

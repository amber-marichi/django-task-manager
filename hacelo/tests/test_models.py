from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone

from hacelo.models import Position, Task, TaskType


class ModelsTests(TestCase):
    def test_position_and_worker_str(self) -> None:
        position = Position.objects.create(
            name="TestPosition",
        )

        worker = get_user_model().objects.create(
            username="testworker",
            first_name="TestFirstName",
            last_name="TestLastName",
            password="$eCr1tT",
            position=position,
        )

        self.assertEqual(str(position), f"{position.name}")

        self.assertEqual(
            str(worker),
            f"{worker.username} ({worker.first_name} {worker.last_name})"
        )

    def test_tasktype_and_task_str(self) -> None:
        tasktype = TaskType.objects.create(
            name="TestTaskType",
        )

        task = Task.objects.create(
            name="TestTask",
            description="to test",
            deadline=timezone.now(),
            is_completed=False,
            priority="1UR",
            task_type=tasktype,
        )

        self.assertEqual(str(tasktype), f"{tasktype.name}")

        self.assertEqual(
            str(task),
            f"{task.id}(Urgent) {task.name}"
        )

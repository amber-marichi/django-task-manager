from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

from taskmanager import settings


class Position(models.Model):
    name = models.CharField(max_length=120, unique=True)

    def __str__(self) -> str:
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(
        to=Position,
        on_delete=models.SET_NULL,
        null=True,
        related_name="workers"
    )

    def __str__(self) -> str:
        return self.username
    
    def get_absolute_url(self):
        return reverse("hacelo:worker-detail", kwargs={"pk": self.pk})


class TaskType(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name


def get_sentinel_task_type():
    return TaskType.objects.get_or_create(name="deleted")[0]


class Task(models.Model):

    PRIORYTY_CHOICES = (
        ("URG", "Small"),
        ("HI", "High"),
        ("MED", "Medium"),
        ("LOW", "Low"),
    )

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    deadline = models.DateTimeField()
    is_completed = models.BooleanField()
    priority = models.CharField(max_length=3, choices=PRIORYTY_CHOICES)
    task_type = models.ForeignKey(
        to=TaskType,
        on_delete=models.SET(get_sentinel_task_type),
        related_name="tasks"
    )
    assignees = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL,
        blank=True,
        related_name="tasks"
    )

    def __str__(self) -> str:
        return f"{self.id}({self.priority}) {self.description}"
    
    def get_absolute_url(self):
        return reverse("hacelo:task-detail", kwargs={"pk": self.pk})

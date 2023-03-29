from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.db.models import Count

from hacelo.models import Task


def index(request: HttpRequest) -> HttpResponse:
    task_list = Task.objects.filter(is_completed=False).select_related("task_type").annotate(Count("assignees")).order_by("priority", "deadline")

    context = {
        "tasks": task_list,
    }

    return render(request, "hacelo/index.html", context)

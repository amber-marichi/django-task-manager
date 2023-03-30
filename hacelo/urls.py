from django.urls import path

from hacelo.views import (
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    WorkerDetailView,
    WorkerCreateView,
    WorkerDeleteView,
    WorkerUpdateView,
    assign_task_to_worker,
    mark_task_completed,
)


urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("task/<int:pk>/detail", TaskDetailView.as_view(), name="task-detail"),
    path("task/create", TaskCreateView.as_view(), name="task-create"),
    path("worker/<int:pk>/detail", WorkerDetailView.as_view(), name="worker-detail"),
    path("worker/create", WorkerCreateView.as_view(), name="worker-create"),
    path("worker/<int:pk>/delete", WorkerDeleteView.as_view(), name="worker-delete"),
    path("worker/<int:pk>/update", WorkerUpdateView.as_view(), name="worker-update"),
    path("task/<int:pk>/assign", assign_task_to_worker, name="task-assign"),
    path("task/<int:pk>/complete", mark_task_completed, name="task-complete"),
]

app_name = "hacelo"

from django.urls import path

from hacelo.views import (
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    WorkerDetailView,
    WorkerCreateView,
    WorkerDeleteView,
    WorkerUpdateView
)


urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("task/<int:pk>/detail", TaskDetailView.as_view(), name="task-detail"),
    path("task/create", TaskCreateView.as_view(), name="task-create"),
    path("worker/<int:pk>/detail", WorkerDetailView.as_view(), name="worker-detail"),
    path("worker/create", WorkerCreateView.as_view(), name="worker-create"),
    path("worker/<int:pk>/delete", WorkerDeleteView.as_view(), name="worker-delete"),
    path("worker/<int:pk>/update", WorkerUpdateView.as_view(), name="worker-update"),
]

app_name = "hacelo"

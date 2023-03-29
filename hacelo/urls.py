from django.urls import path

from hacelo.views import (
    TaskListView,
    TaskDetailView,
    WorkerDetailView,
)


urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("task/<int:pk>/detail", TaskDetailView.as_view(), name="task-detail"),
    path("worker/<int:pk>/detail", WorkerDetailView.as_view(), name="worker-detail"),
]

app_name = "hacelo"

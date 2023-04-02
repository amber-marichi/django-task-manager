from django.urls import path

from hacelo.views import (
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    WorkerDetailView,
    WorkerCreateView,
    WorkerDeleteView,
    WorkerUpdateView,
    WorkerListView,
    TaskTypeCreate,
    assign_task_to_worker,
    mark_task_completed,
)


urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path(
        "tasks/<int:pk>/detail/",
        TaskDetailView.as_view(),
        name="task-detail"
    ),
    path(
        "tasks/create/",
        TaskCreateView.as_view(),
        name="task-create"
    ),
    path(
        "workers/",
        WorkerListView.as_view(),
        name="worker-list"
    ),
    path(
        "workers/<int:pk>/detail/",
        WorkerDetailView.as_view(),
        name="worker-detail"
    ),
    path(
        "workers/create/",
        WorkerCreateView.as_view(),
        name="worker-create"
    ),
    path(
        "workers/<int:pk>/delete/",
        WorkerDeleteView.as_view(),
        name="worker-delete"
    ),
    path(
        "workers/<int:pk>/update/",
        WorkerUpdateView.as_view(),
        name="worker-update"
    ),
    path(
        "tasks/addtype/",
        TaskTypeCreate.as_view(),
        name="tasktype-create"
    ),
    path(
        "tasks/<int:pk>/assign/",
        assign_task_to_worker,
        name="task-assign"
    ),
    path(
        "tasks/<int:pk>/complete/",
        mark_task_completed,
        name="task-complete"
    ),
]

app_name = "hacelo"

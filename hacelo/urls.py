from django.urls import path

from hacelo.views import (
    index,
    TaskDetailView
)


urlpatterns = [
    path("", index, name="index"),
    path("task/<int:pk>/detail", TaskDetailView.as_view(), name="task-detail"),
]

app_name = "hacelo"

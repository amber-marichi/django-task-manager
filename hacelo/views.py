from django.views import generic
from django.db.models import Count, Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model

from hacelo.models import Task, TaskType
from hacelo.forms import (
    TaskSearchForm,
    TaskForm,
    TaskTypeForm,
    WorkerForm,
    WorkerSearchForm,
)


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "hacelo/index.html"
    paginate_by = 5

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = TaskSearchForm(
            initial={"name": name,}
        )
        return context
    
    def get_queryset(self) -> QuerySet:
        queryset = Task.objects.filter(is_completed=False).select_related("task_type").annotate(Count("assignees")).order_by("priority", "deadline")
        form = TaskSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return queryset


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task

    def get_queryset(self) -> QuerySet:
        queryset = super().get_queryset()
        queryset.select_related("task_type")
        return queryset.prefetch_related("assignees__position")


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = get_user_model()
    
    def get_queryset(self) -> QuerySet:
        queryset = super().get_queryset()
        return queryset.prefetch_related("tasks")


class WorkerCreateView(generic.CreateView):
    model = get_user_model()
    form_class = WorkerForm


class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = get_user_model()
    form_class = WorkerForm


class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = get_user_model()
    success_url = reverse_lazy("hacelo:index")


class WorkerListView(generic.ListView):
    model = get_user_model()
    paginate_by = 10
    context_object_name = "workers"

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        context["search_form"] = WorkerSearchForm(
            initial={"username": username,}
        )
        return context

    def get_queryset(self) -> QuerySet:
        queryset = get_user_model().objects.select_related("position").annotate(ongoing=Count('tasks', filter=Q(tasks__is_completed=False)), finished=Count('tasks', filter=Q(tasks__is_completed=True))).order_by("-ongoing") #.annotate(finished=Count('tasks', filter=Q(tasks__is_finished=True)))
        form = WorkerSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                username__icontains=form.cleaned_data["username"]
            )
        return queryset


class TaskTypeCreate(LoginRequiredMixin, generic.CreateView):
    model = TaskType
    form_class = TaskTypeForm
    template_name = "hacelo/task_type_create.html"
    success_url = reverse_lazy("hacelo:task-create")


@login_required
def assign_task_to_worker(request: HttpRequest, pk: int) -> HttpResponse:
    worker = get_user_model().objects.get(id=request.user.id)
    task = Task.objects.get(id=pk)
    if task.assignees.filter(id=request.user.id).exists():
        worker.tasks.remove(pk)
    else:
        worker.tasks.add(pk)
    return HttpResponseRedirect(reverse_lazy("hacelo:task-detail", args=[pk]))


@login_required
def mark_task_completed(request: HttpRequest, pk: int) -> HttpResponse:
    task = Task.objects.get(id=pk)
    task.is_completed = True
    task.save()
    return HttpResponseRedirect(reverse_lazy("hacelo:task-detail", args=[pk]))

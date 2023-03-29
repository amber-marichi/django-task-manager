from django.db.models import Count
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from django.urls import reverse_lazy

from hacelo.models import Task, Worker
from hacelo.forms import TaskSearchForm, WorkerForm


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "hacelo/index.html"
    paginate_by = 10

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


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker


class WorkerCreateView(generic.CreateView):
    model = Worker
    form_class = WorkerForm


class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Worker
    form_class = WorkerForm


class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("hacelo:index")

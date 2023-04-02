from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from hacelo.models import Position, Task, TaskType, Worker


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position",)
    fieldsets = UserAdmin.fieldsets + (
        (("Professional info", {"fields": ("position",)}),)
    )
    list_filter = ("position",)
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Personal info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "email",
                    )
                },
            ),
            (
                "Professional info",
                {
                    "fields": (
                        "position",
                    )
                },
            ),
        )
    )


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "name", "task_type", "priority", "deadline", "is_completed",
    )
    search_fields = ("name",)
    list_filter = ("is_completed", "priority", "task_type",)


admin.site.register(Position)
admin.site.register(TaskType)
admin.site.unregister(Group)

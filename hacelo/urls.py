from django.urls import path

from hacelo.views import index


urlpatterns = [
    path("", index, name="index"),
]

app_name = "hacelo"

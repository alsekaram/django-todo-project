from django.urls import path
from django.views.generic import TemplateView

from todo_list.views import index_view

app_name = "todo_list"

urlpatterns = [
    path("", index_view, name="index"),
]

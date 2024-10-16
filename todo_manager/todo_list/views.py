from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def index_view(request: HttpRequest) -> HttpResponse:
    todo_items = [
        "items 1",
        "items 2",
    ]
    return render(request, "todo_list/index.html", context={"todo_items": todo_items})

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.


def home(request):

    todo = To_do.objects.all()

    context = {"title": "Home Page", "todo": todo}
    return render(request, "index.html", context)


def add_task(request):

    if request.method == "POST":
        data = request.POST

        title = data.get("todo_title")
        task = data.get("todo_task")

        To_do.objects.create(
            todo_title=title,
            todo_task=task,
        )
        return redirect("/")

    context = {"title": "Add Task"}
    return render(request, "Add_task.html", context)


def update_task(request, id):

    x = To_do.objects.get(id=id)

    if request.method == "POST":
        data = request.POST

        title = data.get("todo_title")
        task = data.get("todo_task")

        x.todo_title = title
        x.todo_task = task

        x.save()

        return redirect("/")

    context = {"title": "Update Task", "task": x}
    return render(request, "Update.html", context)


def delete_task(request, id):
    x = To_do.objects.get(id=id)

    x.delete()
    return redirect("/")

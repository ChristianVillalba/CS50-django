from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="priority", min_value=1, max_value=5, )

# Create your views here.
tasks = []

def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })

def addTask (request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/addtask.html",{
                "form": form
            })
    return render(request, "tasks/addtask.html", {
        "form": NewTaskForm()
    })

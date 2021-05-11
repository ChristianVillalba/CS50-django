from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="priority", min_value=1, max_value=5, )

# Create your views here.

#Changed in order to create sessions
#tasks = [] This is a local variable displayed for everybody

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = [ ]
    return render(request, "tasks/index.html", {
        #"tasks": tasks  variable tasks no longer exists
        "tasks":request.session["tasks"]
    })

def addTask (request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            #tasks.append(task)
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/addtask.html",{
                "form": form
            })
    return render(request, "tasks/addtask.html", {
        "form": NewTaskForm()
    })

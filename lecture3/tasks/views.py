from django.shortcuts import render
from django import forms

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="priority", min_value=1, max_value=10, )

# Create your views here.
tasks = ["plan","code","debug"]
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })

def addTask (request):
    return render(request, "tasks/addtask.html", {
        "form": NewTaskForm()
    })

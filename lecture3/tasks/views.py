from django.shortcuts import render

# Create your views here.
tasks = ["plan","code","debug"]
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })

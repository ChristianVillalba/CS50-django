from django.shortcuts import render

# Create your views here.
task = ["ma","me","mi"]
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })
    

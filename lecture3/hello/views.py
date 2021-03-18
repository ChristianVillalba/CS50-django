from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def cristian(request):
    return HttpResponse("This is working, Cristian")

def cthulhu(request):
    return HttpResponse("Ph'nglui mglw'nafh Cthulhu R'lyeh wgah'nagl fhtagn")

# greet using HttpResponse
"""
def greet(request, name):
#takes an additional arg: name
    return HttpResponse(f"Hello,{name.capitalize()}")
    #we are using a python method """
# greet using render
def greet(request, name):
    return render(request, "hello/greet.html",{
        "name": name.capitalize()
    })

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello World!")

def cristian(request):
    return HttpResponse("This is working, Cristian")

def cthulhu(request):
    return HttpResponse("Ph'nglui mglw'nafh Cthulhu R'lyeh wgah'nagl fhtagn")

def greet(request, name): #takes an additional arg: name
    return HttpResponse(f"Hello,{name.capitalize()}")

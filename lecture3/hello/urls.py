from django.urls import path
from . import views
# . the current directory

urlpatterns = [
    path("",views.index, name="index"),
    # "" empty string, no additional args
    path("cristian",views.cristian, name="cristian"),
    path("cthulhu",views.cthulhu, name="cthulhu"),
    #url pattern using placeholders
    path("<str:name>",views.greet, name="greet"),

]

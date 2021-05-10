from django.urls import path
from . import views

app_name = "tasks"
urlpatterns = [
    # "" empty string, no additional args
    path("",views.index, name="index"),
    path("addtask", views.addTask, name="addtask")
]

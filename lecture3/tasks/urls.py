from django.urls import path
from . import views

urlpatterns = [
    # "" empty string, no additional args
    path("",views.index, name="index"),
]

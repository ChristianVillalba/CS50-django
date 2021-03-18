from django.urls import path
from . import views
# . the current directory

urlpatterns = [
    path("",views.index, name="index"),
    # "" empty string, no additional args
]

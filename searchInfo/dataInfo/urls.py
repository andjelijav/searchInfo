from django.urls import path
from django.http import HttpResponse, request

def home(request):
    return HttpResponse("<h1> Dobrodosli </h1>")

urlpatterns = [
    path("",home ),
]
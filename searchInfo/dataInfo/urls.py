from django.urls import path
from .import views




urlpatterns = [
    path("",views.home, name='home' ),
    path("login/",views.loginView, name= 'logovanje'),
    path("registration/", views.registrationView, name='registration'),
    path("homeUser/", views.homeUserView, name='homeUser'),
]
from django.urls import path
from .import views

urlpatterns = [
    path('api/login/', views.login_view),
    path('api/logout/', views.logout_view),
    path('api/signup/', views.signup_view),
    path('api/create/',views.create_user_view),
]
from django.urls import path
from .import views

urlpatterns = [
    path('api/login/', views.login_view, name='login'),
    path('api/logout/', views.logout_view, name='logout'),
    path('api/signup/', views.signup_view),
    path('api/create/',views.create_user_view, name='create'),
    path('api/uploadFile', views.uploadFile_view, name='uploadFile'),
    path('api/uploadSuccess', views.upload, name='uploadSuccess'),
    path('api/adminPage', views.adminUser_view, name='adminPage'),
    path('api/homeUser', views.homeUser_view, name='homeUser'),
    path('api/sheredDocuments', views.shered_view, name='shered'),
    
    
]
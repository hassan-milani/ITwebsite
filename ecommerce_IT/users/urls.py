from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.registerORlogin, name='register'),
    path('logout/', views.logoutUser, name="logout"),
  

]
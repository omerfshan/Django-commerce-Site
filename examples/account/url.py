from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    path('login',views.login,name="login"),
    path('register',views.register,name="register"),
    path('logout',views.login,name="logout"),

   
] 

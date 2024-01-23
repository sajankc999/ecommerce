from django.contrib import admin
from django.urls import path,include
from .views import *
from rest_framework import routers

# router.register("register",registerViewset,basename='register')
# router.register("login",loginViewset,basename="login")
urlpatterns = [
   # path("register",register),
   # path("login/",login),
   path('auth/', include('djoser.urls')),
   path("auth/",include("djoser.urls.authtoken")),

]
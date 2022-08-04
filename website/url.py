from django.contrib import admin
from django.urls import path,include
from .views import home,login,logout,base
urlpatterns = [
    path('', base),
    path('home/',home),
    path('login/',login),
    path('logout/',logout)

]

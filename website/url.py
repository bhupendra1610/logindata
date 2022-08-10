from django.contrib import admin
from django.urls import path,include
from .views import home,login,logout,base
from . import views
urlpatterns = [
    path('', base),
    path('home/',views.home , name='home'),
    path('login/',views.login , name='login'),
    path('logout/',views.logout , name='logout')

]

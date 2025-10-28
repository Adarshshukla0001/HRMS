from django.contrib import admin
from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('adlogin',views.adlogin,name='adlogin'),
    path('emplogin',views.emplogin,name='emplogin'),
    path('validateuser',views.validateuser,name='validateuser'),
    path('validateemp',views.validateemp,name='validateemp'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('services',views.services,name='services'),
    path('logout',views.logout,name='logout')

]
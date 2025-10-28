from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('nfc',views.nfc,name='nfc'),
    path('empfeed',views.empfeed,name='empfeed'),
    path('empleave',views.empleave,name='empleave'),
    path('empsal',views.empsal,name='empsal'),
    path('updateemp',views.updateemp,name='updateemp'),
    path('logout',views.logout,name='logout')
    
   
]
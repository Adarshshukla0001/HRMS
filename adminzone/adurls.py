from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('addemp',views.addemp,name='addemp'),
    path('viewemp',views.viewemp,name='viewemp'),
    path('nfc',views.nfc,name='nfc'),
    path('feed',views.feed,name='feed'),
    path('attend',views.attend,name='attend'),
    path('viewattend',views.viewattend ,name='viewattend'),
    path('sal',views.sal,name='sal'),
    path('leave',views.leave,name='leave'),
    
    path('sendsal',views.sendsal,name='sendsal'),
    path('deleteemp/?P<empid>\d+',views.deleteemp,name='deleteemp'),
    path('accept/?P<empid>\d+',views.accept,name='accept'),
    path('reject/?P<empid>\d+',views.reject,name='reject'),
    path('present/?P<empid>\d+',views.present,name='present'),
    path('ab/?P<empid>\d+',views.ab,name='ab'),
    path('pr/?P<empid>\d+',views.pr,name='pr'),
    path('addsal/?P<empid>\d+',views.addsal,name='addsal'),
    path('send/?P<empid>\d+',views.send,name='send'),
    
]
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('appointment', views.appointment, name='appointment'),
    path('contactus', views.contactus, name='contact'),
    path('explore1', views.explore1, name='explore1'),]
from django.contrib import admin
from django.urls import path

from api import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('home/team/<int:team>/', views.get_team, name='get teams'),
    path('home/simulation/', views.simulation, name='simulation')
]

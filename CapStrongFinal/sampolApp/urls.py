from django.urls import path
from .import views

app_name = 'sampolApp'

urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('dashboard', views.dashboard)
]
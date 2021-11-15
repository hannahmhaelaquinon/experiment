from django.urls import path
from .import views

app_name = 'sampolApp'

urlpatterns = [
    path('', views.home),
    path('index/', views.indexView.as_view(), name="indexView"),
    path('login/', views.loginView.as_view(), name="loginView"),
    path('dashboard/', views.dashboardView.as_view(), name="dashboardView")
]
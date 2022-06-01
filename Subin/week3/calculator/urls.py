from django.urls import path
from calculator import views

urlpatterns = [
    path('', views.main, name="main"),
    path('calculate/', views.calculate, name="calculate"),
]
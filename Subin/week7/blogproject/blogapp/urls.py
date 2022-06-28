from django.urls import path
from blogapp import views

urlpatterns = [
    path('', views.Posts.as_view()),
    path('<int:pk>/', views.Details.as_view()),
]

from django.urls import path
from wordcounter import views

urlpatterns = [
    path('', views.main, name="word_main"),
    path('wordcount/', views.wordcount, name="wordcount"),
]
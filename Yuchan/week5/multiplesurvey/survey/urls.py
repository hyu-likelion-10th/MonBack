from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name= "main"),
    path('save', views.save, name="save"),
    path('result/<int:question_id>', views.result, name="result"),
]
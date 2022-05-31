from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name= "main"),
    path('save_survey', views.save_survey, name="save"),
    path('show_result/<int:question_id>', views.show_result, name="result"),
]
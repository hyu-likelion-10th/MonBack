from django.db import models

# Create your models here.
class Survey(models.Model):
    choice = models.CharField(max_length=50)

class Answer(models.Model):
    answer = models.ForeignKey(Survey, on_delete=models.CASCADE)
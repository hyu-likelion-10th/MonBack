from django.db import models

# Create your models here.
class Survey(models.Model):
    question = models.TextField()
    answer_1 = models.CharField(max_length=50)
    answer_2 = models.CharField(max_length=50)
    answer_3 = models.CharField(max_length=50)
    answer_4 = models.CharField(max_length=50)
    def __str__(self):
        return self.question

class Answer(models.Model):
    survey_index = models.IntegerField()
    answer = models.CharField(max_length=50)
    def __str__(self):
        return self.answer
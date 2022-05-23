from django.db import models

class Survey(models.Model):
  id = models.AutoField(primary_key=True)
  question = models.TextField(null=False)
  select0 = models.TextField(null=True)
  select1 = models.TextField(null=True)
  select2 = models.TextField(null=True)
  select3 = models.TextField(null=True)

  def __str__(self):
    return self.question

class Answer(models.Model):
  id = models.AutoField(primary_key=True)
  survey_id = models.IntegerField()
  selected = models.TextField()

# Create your models here.

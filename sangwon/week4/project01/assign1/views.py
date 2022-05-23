from select import select
from django.shortcuts import render
from .models import Survey, Answer

def index(request):
  if Survey.objects.get_queryset().exists() :
    survey = Survey.objects.filter()[0]
    return render(request, 'main.html', {'survey' : survey})
  return render(request, 'main.html')

def save(request):
  print(request.POST)
  id = request.POST["id"]
  select = request.POST["select"]
  submit = Answer(survey_id = id, selected = select)
  submit.save()
  return render(request, "complete.html")

def result(request, id):
  survey = Survey.objects.filter(id=id)[0]
  results = {
    survey.select0 : 0,
    survey.select1 : 0,
    survey.select2 : 0,
    survey.select3 : 0,
  }

  answers = Answer.objects.filter(survey_id=id)
  for ans in answers:
    results[ans.selected] += 1
  return render(request, 'result.html', {'results' : results})
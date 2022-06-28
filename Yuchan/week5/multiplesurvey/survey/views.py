from re import T
import re
from django.shortcuts import redirect, render

# Create your views here.
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from survey.models import Survey, Answer
# Create your views here.
def main(request):
    survey = Survey.objects.all()
    return render(request, 'main.html', {'survey': survey})

@csrf_protect
def save(request):
    survey_idx = request.POST["survey_idx"]
    dto = Answer(survey_idx=survey_idx, ans=request.POST["num"])
    dto.save()
    return render(request, "complete.html")

@csrf_protect
def result(request, question_id):
    answers = Answer.objects.filter(survey_idx=question_id)
    orig_answers = Survey.objects.filter(survey_idx=question_id)[0]
    result = {
        orig_answers.ans1: 0,
        orig_answers.ans2: 0,
        orig_answers.ans3: 0,
        orig_answers.ans4: 0,
    }

    for ans in answers:
        result[ans.ans] += 1

    return render(request, "result.html", {'result': result})

def new(request):
    return render(request, 'new.html')

def create(request):
    tmp_survey = Survey()
    tmp_survey.question = request.POST['question']
    tmp_survey.ans1 = request.POST['ans1']
    tmp_survey.ans2 = request.POST['ans2']
    tmp_survey.ans3 = request.POST['ans3']
    tmp_survey.ans4 = request.POST['ans4']
    tmp_survey.save()

    return redirect('main')
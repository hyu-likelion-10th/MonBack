from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from survey.models import Survey, Answer
# Create your views here.
def main(request):
    survey = Survey.objects.filter(status='y').order_by('-survey_idx')[0]

    return render(request, 'main.html', {'survey': survey})

@csrf_protect
def save_survey(request):
    survey_idx = request.POST["survey_idx"]
    dto = Answer(survey_idx=survey_idx, ans=request.POST["num"])
    dto.save()
    return render(request, "success.html")

@csrf_protect
def show_result(request, question_id):
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
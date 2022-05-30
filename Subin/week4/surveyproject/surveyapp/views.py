from django.shortcuts import render
from .models import Survey, Answer

# Create your views here.
def main(request):
    surveys = Survey.objects.all()
    return render(request, 'main.html', {'surveys': surveys})

def result(request, survey_id):
    if request.method == 'GET':
        answers = Answer.objects.filter(survey_index=survey_id)
        original_answers = Survey.objects.filter(id=survey_id)[0]
        results = {
            original_answers.answer_1: 0,
            original_answers.answer_2: 0,
            original_answers.answer_3: 0,
            original_answers.answer_4: 0,
        }

        for answer in answers:
            results[answer.answer] += 1
        
        return render(request, 'result.html', {'results': results})

def votecomplete(request, survey_id):
    if request.method == 'POST':
        data = Answer(survey_index=survey_id, answer=request.POST['choice'])
        data.save()
    return render(request, 'votecompletion.html')
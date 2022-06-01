from django.shortcuts import redirect, render
from .models import Survey, Answer

# Create your views here.
def main(request):
    if Survey.objects.exists():
        surveys = Survey.objects.all()
        return render(request, 'main.html', {'surveys': surveys})
    else:
        return render(request, 'main.html', {'surveys': []})

def save(request, survey_id):
    if request.method == 'POST':
        data = Answer(survey_index=survey_id, answer=request.POST['choice'])
        data.save()
    return render(request, 'complete.html')

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

def new(request):
    return render(request, 'new.html')

def create(request):
    if request.method == 'POST':
        survey1 = Survey()
        survey1.question = request.POST['question']
        survey1.answer_1 = request.POST['answer_1']
        survey1.answer_2 = request.POST['answer_2']
        survey1.answer_3 = request.POST['answer_3']
        survey1.answer_4 = request.POST['answer_4']
        survey1.save()
    return redirect('main')



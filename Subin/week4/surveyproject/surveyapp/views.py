import re
from django.shortcuts import render
from .models import Survey, Answer

# Create your views here.
def main(request):
    return render(request, 'main.html')

def result(request):
    if request.method == 'GET':
        surveys = Survey.objects.get(id=request.GET['survey_id'])
        return render(request, 'result.html', {'surveys': surveys})

def votecomplete(request):
    if request.method == 'POST':
        data = Survey()
        data.choice = request.POST['value']
        data.save()
    return render(request, 'votecompletion.html')
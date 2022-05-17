from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'main.html')

def calculate(request):
    value = request.GET['result']
    return render(request, 'calculator.html', {"resultValue": eval(value)})
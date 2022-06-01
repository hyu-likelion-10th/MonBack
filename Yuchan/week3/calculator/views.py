from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'main.html')

def calculator(request):
    expression = request.GET['expression']
    result = eval(expression)
    return render(request, 'calculator.html', {'result':result})
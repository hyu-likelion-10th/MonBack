from django.shortcuts import render

# Create your views here.
def main(request):
  return render(request, 'main.html')

def calculator(request):
  exp = request.GET['expression']
  result = eval(exp)
  return render(request, 'calculator.html', {"result": result})
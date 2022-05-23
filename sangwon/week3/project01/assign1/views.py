from django.shortcuts import render

def index(request):
    return render(request, 'main.html')

def postgood(request):
    val = request.GET['val']
    data = 'ERROR'
    try:
      data = eval(val)
    except: pass
    return render(request, 'calculator.html', { 'val' : data })
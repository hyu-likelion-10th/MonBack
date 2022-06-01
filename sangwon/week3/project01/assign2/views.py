from django.shortcuts import render

# Create your views here.

def index(request):
  return render(request, 'main2.html')

def postgood(request):
  string = request.GET['story']
  strArr = string.split()
  dic = {}
  for s in strArr:
    try:
      dic[s] += 1
    except:
      dic[s] = 1
  result = ""
  for key in dic.keys():
    result += f"{key} : {dic[key]},\n"
  print(dic)
  return render(request, 'assign2.html', { 'result' : result})
from django.shortcuts import render

# Create your views here.
def main(request):
  return render(request, 'main.html')

def wordcount(request):
  dic = {}
  sentence = request.GET['wordcount']
  count = len(sentence.split())
  arr = sentence.split()
  for i in arr:
    if (i in dic):
      dic[i] += 1
    else:
      dic[i] = 1
  arr = [1, 2, 3, 4, 5]
  data = dict(count=count, sentence=sentence, dic=dic, arr=arr)
  return render(request, 'wordcount.html', {"data": data})

  
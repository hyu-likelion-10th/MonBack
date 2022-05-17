from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'wordcounter_main.html')

def wordcount(request):
    dictionary = {}
    inputText = request.GET['inputstring']
    word_list = inputText.split()
    for i in word_list:
        dictionary[i] = 0
    for j in word_list:
        if dictionary[j] == 0:
            dictionary[j] = 1
        else:
            dictionary[j] += 1
    word_count = ""
    for word, amount in dictionary.items():
        word_count += "{} - {}".format(word, amount)
        word_count += "\n"

    return render(request, 'wordcount.html',
    {"result": len(inputText.split()), 
    "plaintext": inputText,
    "wordcount": word_count
    })
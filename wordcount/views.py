from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']

    wordlist = (fulltext.split())

    individual_word_count = {}

    for word in wordlist:
        if word in individual_word_count:
            individual_word_count[word] += 1
        else:
            individual_word_count[word] = 1

    sortedwords = sorted(individual_word_count.items(), key = operator.itemgetter(1), reverse=True)


    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist), 'words': sortedwords})

def about(request):
    return render(request, 'about.html')
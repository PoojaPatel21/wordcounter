from django.http import HttpResponse
from django.shortcuts import render 


def home(request):
	return render(request, 'home.html')

def count(request):
	fulltext = request.GET['entertext']
	words = fulltext.split()
	count = len(words)


	return render(request, 'count.html', {'fulltext':fulltext,'count':count})

def about(request):
	return render(request, 'about.html')

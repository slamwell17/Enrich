from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'search/search_results.html')

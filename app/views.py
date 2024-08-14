from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def starbucks(request):
    return HttpResponse('Worst Chai is Avaialable in Starbucks')
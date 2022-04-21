from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('We\'re going to do what we do every night Pinky...try to take over the world!' 
        '\n NARF!')

# Create your views here.

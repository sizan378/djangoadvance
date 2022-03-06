from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def djnago_dj(request):
    return HttpResponse("Django Coursee Part")

def institute(request):
    return HttpResponse("Django Institute Part")

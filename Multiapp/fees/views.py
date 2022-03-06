from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def  amount(request):
    return HttpResponse('Total Amount of fees')

def fees_count(request):
    return HttpResponse("Total fees Count")

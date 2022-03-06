from django.shortcuts import render
from django.http import JsonResponse


def api_home(reqeust):
    return JsonResponse({"Message": "Hi this is Django"})

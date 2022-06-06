from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse,HttpResponse
from .models import Student
from .serializers import StudentSerializers


def api_home(reqeust):
    return JsonResponse({"Message": "Hi this is Django"})

def student(request):
    stu = Student.objects.all()
    serilizer = StudentSerializers(stu, many=True)
    json_data = JSONRenderer().render(serilizer.data)
    # return JsonResponse(serilizer.data, safe=False)
    return HttpResponse(json_data,content_type='application/json')
from django.shortcuts import render

def django_learner(request):
    list = {
        'name': 'Django',
        'fees': '3000',
        'duration': '3 month',
    }
    return render(request,'course/django.html', context = list)

def python_learner(request):
    return render(request,'course/python.html')

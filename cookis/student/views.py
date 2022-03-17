from urllib import response
from django.shortcuts import render



def setcookie(request):
    response = render(request, 'student/setcookis.html')
    response.set_cookie('name','sizan')
    return response


def getcookie(request):
    # name = request.COOKIES['name']
    name = request.COOKIES.get('name','not set Cookies')
    return render(request, 'student/getcookis.html',{'name':name})

def delcookie(request):
    response = render(request, 'student/delcookis.html')
    response.delete_cookie('name')
    return response
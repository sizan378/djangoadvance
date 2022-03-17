
from django.urls import path
from .views import delcookie, setcookie, getcookie, delcookie

urlpatterns = [
    path('setcookie/',setcookie, name='setcookie'),
    path('getcookie/',getcookie,name='getcookie'),
    path('delcookie/',delcookie,name='delcoookie'),
]
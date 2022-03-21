
from django.urls import path
from .views import setsession,getsession,delsession

urlpatterns = [
    path('setsession/',setsession, name='setsession'),
    path('getsession/',getsession,name='getsession'),
    path('delsession/',delsession,name='delsession'),
]
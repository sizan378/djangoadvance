from django.urls import path
from .views import django_learner, python_learner

urlpatterns = [
    path('djangodj/', django_learner),
    path('djangopy/', python_learner)
]

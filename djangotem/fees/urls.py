from urllib.parse import urlparse
from django.urls import path
from . import views


urlpatterns = [
    path('feesdj/', views.feesdj),
    path('feespy/',views.feespy),
]

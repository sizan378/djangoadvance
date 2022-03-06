
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cor/', include("course.urls")),
    path('fe/',include("fees.urls")),
]

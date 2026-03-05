"""
URL configuration for api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST', 'PUT','DELETE'])
def hello(request):
    if request.method == 'GET':
        return Response({
            "message": "Hello xd",
            "method": "Fue por GET"
        })

    if request.method == 'POST':
        return Response({
            "message": "Hello xd",
            "method": "Fue por POST"
        })

    if request.method == 'PUT':
        return Response({
            "message": "Hello xd",
            "method": "Fue por PUT"
        })

    if request.method == 'DELETE':
        return Response({
            "message": "Hello xd",
            "method": "Fue por DELETE"
        })


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', hello),
    path('api/cars/', include('cars.urls'))
]

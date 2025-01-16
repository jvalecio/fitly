from django.urls import path, include
from django.contrib import admin 
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets



# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    
    #path('', include('fitly.api.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('fitly.api.urls')),
]

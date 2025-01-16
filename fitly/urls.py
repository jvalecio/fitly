from django.urls import path, include
from django.contrib import admin 


# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('fitly.api.urls')),
    path('demo/', include('fitly.demo.urls')),
]

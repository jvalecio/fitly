from django.shortcuts import render
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from .views import ProjectViewset, Test
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

router = DefaultRouter()
router.register('router', ProjectViewset, basename='project')
urlpatterns = router.urls
    
urlpatterns = [path('', include(router.urls)),
    path('fin/',Test.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    ]
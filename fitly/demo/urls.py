
from django.urls import path
from fitly.demo import views

urlpatterns = [path('', views.demo, name='demo'),
               ]
from django.shortcuts import render
from rest_framework import viewsets,permissions
from .models import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.
class ProjectViewset(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    #queryset = Project.objects.all()

    def list(self, request):
        pass


class Test(APIView):
    def get(self, request):
        return Response({"resultado": 2}, status=status.HTTP_200_OK)
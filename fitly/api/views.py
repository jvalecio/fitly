from .models import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
    
class Test(APIView):
    def get(self, request):
        return Response({"resultado": 2}, status=status.HTTP_200_OK)
    

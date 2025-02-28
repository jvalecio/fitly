from django.shortcuts import render
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
)
from rest_framework.viewsets import GenericViewSet
from .serializers import IngredientSerializer
from .models import IngredientModel

# Create your views here.
class IngredientViewSet(GenericViewSet,
                        CreateModelMixin,
                        RetrieveModelMixin,
                        UpdateModelMixin,
                        ListModelMixin):
    
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = IngredientSerializer
    queryset = IngredientModel.objects.all()
    
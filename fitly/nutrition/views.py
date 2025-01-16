from django.shortcuts import render

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
    
    serializer_class = IngredientSerializer
    queryset = IngredientModel.objects.all()
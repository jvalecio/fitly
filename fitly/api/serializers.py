from rest_framework import serializers
from .models import *

class ProjectSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Project
        fields = ('id','name','projectmanager', 'start_date','employees', 'end_date', 'comments', 'status')

class ProjectSerializer(serializers.Serializer):
    class Meta:
        model = ProjectManager
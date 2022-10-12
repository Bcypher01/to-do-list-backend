from pyexpat import model
from rest_framework.serializers import ModelSerializer
from .models import Status, ToDo

class StatusSerializer(ModelSerializer):
    class Meta:
        model = Status
        fields = ['name']

class ToDoSerializer(ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'

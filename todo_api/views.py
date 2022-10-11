from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from todo_api.models import ToDo
from todo_api.serializers import ToDoSerializer

# Create your views here.

class ToDoApiView(APIView):
    def get(self, request):
        toDo = ToDo.objects.all()
        serializer = ToDoSerializer(toDo, many=True)
        return Response(serializer.data)
        
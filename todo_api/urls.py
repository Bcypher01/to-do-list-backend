from posixpath import basename
from django.urls import path, include
from . import views

urlpatterns = [
    path('todo/', views.ToDoApiView.as_view()),
]

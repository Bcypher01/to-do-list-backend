from posixpath import basename
from django.urls import path, include
from . import views

urlpatterns = [
    path('status/', views.StatusApiView.as_view()),
    path('todo/', views.ToDoApiView.as_view()),
]

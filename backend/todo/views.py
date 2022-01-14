from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from rest_framework import viewsets # provides the implementation for CRUD operations by default.
from .serializers import TodoSerializer
from .models import Todo

# Create your views here.

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
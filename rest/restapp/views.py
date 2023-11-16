from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TaskSerializer, UserSerializer
from .models import Task
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView

class Createuserview(CreateAPIView):
    model = get_user_model()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

class TaskViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all().order_by('-date_created')
    serializer_class = TaskSerializer

class DueTaskViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Task.objects.filter(completed=False).order_by('-date_created')
    serializer_class = TaskSerializer

class CompletedTaskViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Task.objects.filter(completed=True).order_by('-date_created')
    serializer_class = TaskSerializer

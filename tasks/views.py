from django.shortcuts import render
from .serializers import RegisterSerializer, TaskSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics, filters, status
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Task
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from datetime import date, timedelta
from django.shortcuts import get_object_or_404

# Create your views here.

@api_view(['POST'])
def register_user(request):
    data = request.data
    serializer = RegisterSerializer(data = data)
    
    if serializer.is_valid():
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user = user)
        return Response({'token': token.key})
    
    return Response(serializer.errors)

@api_view(['POST'])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)

    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    
    return Response({'error': 'Invalid credentials'})

# @permission_classes([IsAuthenticated])
# class TaskListCreateView(generics.ListCreateAPIView):
#     serializer_class = TaskSerializer

#     def get_queryset(self):
#         user = self.request.user
#         queryset = Task.objects.filter(assigned_to=user)

#         status = self.request.query_params.get('status')
#         due_before = self.request.query_params.get('due_before')

#         if status:
#             queryset = queryset.filter(status=status)

#         if due_before:
#             queryset = queryset.filter(due_date__lte=due_before)

#         return queryset
    
#     def perform_create(self, serializer):
#         serializer.save(assigned_to=self.request.user)

# @permission_classes([IsAuthenticated])
# class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = TaskSerializer

#     def get_queryset(self):
#         return Task.objects.filter(assigned_to=self.request.user)

class TaskListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        tasks = Task.objects.filter(assigned_to=user)

        status_param = request.query_params.get('status')
        due_before = request.query_params.get('due_before')

        if status_param:
            tasks = tasks.filter(status=status_param)
        if due_before:
            tasks = tasks.filter(due_date__lte=due_before)

        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        data = request.data
        user = request.user
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save(assigned_to=user)
            return Response(serializer.data)
        return Response(serializer.errors)
    

class TaskDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk, user):
        return get_object_or_404(Task, pk=pk, assigned_to=user)
    
    def get(self, request, pk):
        user = request.user
        task = self.get_object(pk, user)
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    
    def put(self, request, pk):
        task = self.get_object(pk, request.user)
        serializer = TaskSerializer(task, data=request.data)

        if serializer.is_valid():
            serializer.save(assigned_to=request.user)
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, request, pk):
        task = self.get_object(pk, request.user)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
# Add new class
@permission_classes([IsAuthenticated])
class TaskTimelineView(APIView):
    def get(self, request):
        user = request.user
        today =  date.today()
        yesterday = today - timedelta(days=1)
        tomorrow = today + timedelta(days=1)

        tasks_yest = Task.objects.filter(assigned_to=user, due_date=yesterday)
        tasks_to = Task.objects.filter(assigned_to=user, due_date=today)
        task_tom = Task.objects.filter(assigned_to=user, due_date=tomorrow)

        data = {
            'yesterday': TaskSerializer(tasks_yest, many=True).data,
            'today': TaskSerializer(tasks_to, many=True).data,
            'tomorrow': TaskSerializer(task_tom, many=True).data
        }
        return Response(data)


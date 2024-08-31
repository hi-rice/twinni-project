from rest_framework import viewsets
from django.shortcuts import render, redirect
from .models import Task
from .serializers import TaskSerializer
from .forms import TaskForm

# API ViewSet
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

def create_task_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # 작업 목록 페이지로 리다이렉트
    else:
        form = TaskForm()

    return render(request, 'tasks/create_task.html', {'form': form})

# Task 목록을 보여주는 View
def task_list_view(request):
    tasks = Task.objects.all()  # 모든 Task를 가져옵니다.
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

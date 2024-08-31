from django.utils import timezone
from rest_framework import viewsets
from .models import Robot
from .serializers import RobotSerializer
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RobotForm

class RobotViewSet(viewsets.ModelViewSet):
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer

def robot_status_view(request):
    robots = Robot.objects.all()
    return render(request, 'robots/robot_status.html', {'robots': robots})


def robot_create_view(request):
    if request.method == 'POST':
        form = RobotForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('robot_status')  # 로봇 상태 모니터링 페이지로 리다이렉트
    else:
        form = RobotForm()

    return render(request, 'robots/robot_form.html', {'form': form})


# 로봇 수정 뷰
def robot_update_view(request, robot_id):
    robot = get_object_or_404(Robot, id=robot_id)
    if request.method == 'POST':
        form = RobotForm(request.POST, instance=robot)
        if form.is_valid():
            form.save()
            return redirect('robot_status')
    else:
        form = RobotForm(instance=robot)

    return render(request, 'robots/robot_form.html', {'form': form})


def robot_delete_view(request, robot_id):
    robot = get_object_or_404(Robot, id=robot_id)
    if request.method == 'POST':
        robot.delete()
        return redirect('robot_status')

    return render(request, 'robots/robot_confirm_delete.html', {'robot': robot})

def perform_maintenance_view(request, robot_id):
    robot = get_object_or_404(Robot, id=robot_id)
    if request.method == 'POST':
        robot.last_maintenance_date = timezone.now()
        robot.maintenance_due = False
        robot.save()
        return redirect('robot_status')
    return render(request, 'robots/perform_maintenance.html', {'robot': robot})

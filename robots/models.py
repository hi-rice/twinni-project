from django.db import models
from django.utils import timezone

class Robot(models.Model):
    STATUS_CHOICES = (
        ('idle', 'Idle'),
        ('busy', 'Busy'),
        ('charging', 'Charging'),
    )

    name = models.CharField(max_length=100)
    model_number = models.CharField(max_length=100, unique=True, blank=True)  # model_number 필드
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    location = models.CharField(max_length=100)
    battery_level = models.IntegerField()
    temperature = models.FloatField(default=0.0)  # 로봇의 온도 필드 추가
    last_maintenance_date = models.DateTimeField(null=True, blank=True)  # 마지막 유지보수 날짜
    maintenance_due = models.BooleanField(default=False)  # 유지보수 필요 여부

    def save(self, *args, **kwargs):
        # model_number 자동 생성
        if not self.model_number:  # model_number가 비어 있을 때만 자동 생성
            last_robot = Robot.objects.all().order_by('id').last()
            if last_robot:
                last_number = int(last_robot.model_number[1:])
                new_number = last_number + 1
            else:
                new_number = 1
            self.model_number = f'R{str(new_number).zfill(3)}'

        # 유지보수 알림 조건
        if self.battery_level < 20 or self.temperature > 80:
            self.maintenance_due = True
        else:
            self.maintenance_due = False

        super(Robot, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

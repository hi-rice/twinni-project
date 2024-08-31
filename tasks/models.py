from django.db import models
from robots.models import Robot
from django.utils import timezone

class Task(models.Model):
    TASK_TYPES = (
        ('delivery', 'Delivery'),
        ('order_picking', 'Order Picking'),
    )

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    )

    PRIORITY_CHOICES = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    )

    robot = models.ForeignKey(Robot, on_delete=models.CASCADE)
    task_type = models.CharField(max_length=50, choices=TASK_TYPES)
    destination = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    priority = models.CharField(max_length=50, choices=PRIORITY_CHOICES, default='medium')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.task_type} - {self.destination}'

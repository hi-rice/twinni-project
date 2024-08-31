from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    role = models.CharField(max_length=30, default='user')  # 기본값을 'user'로 설정

class UserEmailSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_host = models.CharField(max_length=100)
    email_port = models.IntegerField()
    email_use_tls = models.BooleanField(default=True)
    email_host_user = models.EmailField()
    email_host_password = models.CharField(max_length=100)
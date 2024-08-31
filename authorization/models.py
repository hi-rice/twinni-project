from django.db import models
from users.models import User

class Permission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    can_edit_profile = models.BooleanField(default=True)
    can_manage_robots = models.BooleanField(default=False)
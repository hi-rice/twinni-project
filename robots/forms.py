from django import forms
from .models import Robot

class RobotForm(forms.ModelForm):
    class Meta:
        model = Robot
        fields = ['name', 'model_number', 'status', 'location', 'battery_level', 'temperature']

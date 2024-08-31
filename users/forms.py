from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, UserEmailSettings

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class RoleUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['role']

class UserEmailSettingsForm(forms.ModelForm):
    class Meta:
        model = UserEmailSettings
        fields = ['email_host', 'email_port', 'email_use_tls', 'email_host_user', 'email_host_password']

class SignUpForm(UserCreationForm):
    role = forms.CharField(max_length=30, required=True, initial='user')

    class Meta:
        model = User
        fields = ['username', 'email', 'role']

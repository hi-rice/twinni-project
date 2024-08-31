from rest_framework import viewsets
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView
from .models import User, UserEmailSettings
from .serializers import UserSerializer
from .forms import UserForm, UserEmailSettingsForm, SignUpForm, RoleUpdateForm
from django.core.mail import send_mail
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test

# API ViewSet
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# 사용자 목록을 보여주는 ListView
class UserListView(ListView):
    model = User
    template_name = 'users/user_list.html'

# 사용자 목록을 보여주는 함수형 뷰
def user_list_view(request):
    users = User.objects.all()  # 모든 사용자 쿼리셋
    return render(request, 'users/user_list.html', {'users': users})

# 사용자를 생성하는 CreateView
class UserCreateView(CreateView):
    model = User
    template_name = 'users/user_form.html'
    fields = ['username', 'email', 'password']

# 사용자 생성 폼을 처리하는 함수형 뷰
def user_create_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()

    return render(request, 'users/user_form.html', {'form': form})

# 사용자별 이메일 설정을 저장하는 뷰
def email_settings_view(request):
    if request.method == 'POST':
        form = UserEmailSettingsForm(request.POST)
        if form.is_valid():
            settings = form.save(commit=False)
            settings.user = request.user
            settings.save()
            return redirect('email_test')  # 이메일 설정 저장 후 테스트로 리다이렉트
    else:
        form = UserEmailSettingsForm()

    return render(request, 'users/email_settings.html', {'form': form})

# 저장된 이메일 설정을 사용하여 테스트 이메일을 전송하는 뷰
def email_test_view(request):
    settings = UserEmailSettings.objects.get(user=request.user)

    # 이메일 전송 시 사용자 설정 사용
    send_mail(
        'Test Email',
        'This is a test email.',
        settings.email_host_user,
        ['recipient@example.com'],  # 수신자 이메일
        fail_silently=False,
        auth_user=settings.email_host_user,
        auth_password=settings.email_host_password,
        connection=None,
        html_message=None
    )

    return render(request, 'users/email_test_done.html')

# 회원 가입 뷰
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # 가입 후 자동으로 로그인 시킴
            return redirect('home')  # 홈 페이지로 리다이렉트
    else:
        form = SignUpForm()

    return render(request, 'users/signup.html', {'form': form})

def update_role_view(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        form = RoleUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')  # 역할 수정 후 사용자 목록으로 리다이렉트
    else:
        form = RoleUpdateForm(instance=user)

    return render(request, 'users/update_role.html', {'form': form})

@login_required
def mypage_view(request):
    user = request.user

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('mypage')  # 수정 후 다시 마이페이지로 리다이렉트
    else:
        form = UserForm(instance=user)

    return render(request, 'users/mypage.html', {'form': form})

# 관리자만 접근할 수 있도록 설정
def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin)
def update_user_role_view(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        form = RoleUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')  # 역할 수정 후 사용자 목록으로 리다이렉트
    else:
        form = RoleUpdateForm(instance=user)

    return render(request, 'users/update_role.html', {'form': form})

@login_required
def delete_user_view(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        logout(request)  # 계정 삭제 후 로그아웃
        return redirect('home')  # 홈 페이지로 리다이렉트

    return render(request, 'users/delete_confirm.html')

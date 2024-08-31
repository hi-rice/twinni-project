from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet
from robots.views import RobotViewSet, robot_status_view, perform_maintenance_view
from robots.views import robot_create_view, robot_update_view, robot_delete_view
from tasks.views import create_task_view, task_list_view, TaskViewSet
from notifications.views import NotificationViewSet
from authorization.views import PermissionViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from config.views import home
from django.contrib.auth import views as auth_views

# DefaultRouter 인스턴스 생성
router = DefaultRouter()

# 각 ViewSet을 라우터에 등록
router.register(r'users', UserViewSet)
router.register(r'robots', RobotViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'notifications', NotificationViewSet)
router.register(r'permissions', PermissionViewSet)

# URL 패턴 설정
urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # API 엔드포인트를 라우터와 연결
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),  # 로그인 URL
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),  # 로그아웃 URL
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT 토큰 발급
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # JWT 토큰 갱신
    path('email-settings/', user_views.email_settings_view, name='email_settings'),
    path('email-test/', user_views.email_test_view, name='email_test'),
    path('signup/', user_views.signup_view, name='signup'),
    path('users/', user_views.user_list_view, name='user_list'),
    path('update-role/<int:user_id>/', user_views.update_role_view, name='update_role'),
    path('mypage/', user_views.mypage_view, name='mypage'),
    path('admin/update-role/<int:user_id>/', user_views.update_user_role_view, name='update_user_role'),  # 관리자 전용 역할 변경 URL
    path('delete-account/', user_views.delete_user_view, name='delete_account'),  # 회원탈퇴 URL 추가
    path('robots/status/', robot_status_view, name='robot_status'),
    path('robots/add/', robot_create_view, name='robot_add'),
    path('robots/<int:robot_id>/edit/', robot_update_view, name='robot_edit'),
    path('robots/<int:robot_id>/delete/', robot_delete_view, name='robot_delete'),
    path('robots/<int:robot_id>/perform_maintenance/', perform_maintenance_view, name='perform_maintenance'),
    path('tasks/create/', create_task_view, name='create_task'),
    path('tasks/', task_list_view, name='task_list'),  # 작업 목록 뷰
]

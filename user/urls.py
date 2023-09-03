from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from user.apps import UserConfig
from user.views import RegistertView, UserProfileView, check_email, password

app_name = UserConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegistertView.as_view(), name='register'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('check_email/', check_email, name='check_email'),
    path('password/', password, name='password'),
]

from django.urls import path, re_path
from .views.login_view import login, do_login
from .views.dashboard_view import dashboard

urlpatterns = [
    path('login', login),
    path('dologin', do_login),
    path('dashboard', dashboard)
]

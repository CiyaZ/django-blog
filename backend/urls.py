from django.urls import path, re_path
from .views.login_view import login, do_login
from .views.dashboard_view import dashboard
from .views.blog_list_view import blog_list, delete_blog

urlpatterns = [
    path('login', login),
    path('dologin', do_login),
    path('dashboard', dashboard),
    path('blogs', blog_list),
    path('blogs/delete', delete_blog),
]

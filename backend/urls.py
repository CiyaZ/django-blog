from django.urls import path, re_path
from .views.login_view import login, do_login
from .views.dashboard_view import dashboard
from .views.blog_list_view import blog_list, delete_blog, edit_blog, add_blog, update_blog
from .views.category_list_view import category_list, add_category, delete_category

urlpatterns = [
    path('login', login),
    path('dologin', do_login),
    path('dashboard', dashboard),
    path('blogs', blog_list),
    path('blogs/edit', edit_blog),
    path('blogs/add', add_blog),
    path('blogs/update', update_blog),
    path('blogs/delete', delete_blog),
    path('categories', category_list),
    path('categories/new', add_category),
    path('categories/delete', delete_category),
]

from django.urls import path, re_path
from .views.login_view import login, do_login, do_logout
from .views.dashboard_view import dashboard
from .views.blog_list_view import blog_list, delete_blog, edit_blog, add_blog, update_blog
from .views.category_list_view import category_list, add_category, delete_category
from .views.author_info_view import author_info, author_info_update
from .views.password_edit_view import password_edit, password_update
from .views.site_config_view import site_config_edit, site_config_update

urlpatterns = [
    path('login', login),
    path('dologin', do_login),
    path('dologout', do_logout),
    path('dashboard', dashboard),
    path('blogs', blog_list),
    path('blogs/edit', edit_blog),
    path('blogs/add', add_blog),
    path('blogs/update', update_blog),
    path('blogs/delete', delete_blog),
    path('categories', category_list),
    path('categories/new', add_category),
    path('categories/delete', delete_category),
    path('author', author_info),
    path('author/update', author_info_update),
    path('password/edit', password_edit),
    path('password/update', password_update),
    path('config/edit', site_config_edit),
    path('config/update', site_config_update),
]

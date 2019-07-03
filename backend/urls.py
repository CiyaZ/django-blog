"""后台系统路由
"""
from django.urls import path
from backend.views.login_view import login, do_login, do_logout
from backend.views.dashboard_view import dashboard
from backend.views.blog_list_view import blog_list, delete_blog, edit_blog, add_blog, update_blog
from backend.views.category_list_view import category_list, add_category, delete_category
from backend.views.author_info_view import author_info, author_info_update
from backend.views.password_edit_view import password_edit, password_update
from backend.views.site_config_view import site_config_edit, site_config_update
from backend.views.site_statistics_view import site_statistics, blog_statistics_query, access_statistics_query
from backend.views.site_tools_view import site_tools, do_generate_sitemap
from backend.views.install_view import install, do_install

urlpatterns = [
    path('login', login),
    path('dologin', do_login),
    path('dologout', do_logout),
    path('', dashboard),
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
    path('tools', site_tools),
    path('tools/generate', do_generate_sitemap),
    path('statistics', site_statistics),
    path('statistics/blog_query', blog_statistics_query),
    path('statistics/access_query', access_statistics_query),
    path('install', install),
    path('install/init', do_install),
]

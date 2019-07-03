"""登录拦截器
用于拦截未授权请求，拦截可配置为仅后台和全站，
仅后台只拦截对管理后台的请求，
全站拦截除了登录页面的全部请求，用于私有日记等内容，
实际部署时静态资源由Nginx处理，不拦截
"""
from django.http import HttpResponseRedirect


class LoginMiddleware:
    """登录拦截器"""

    def __init__(self, get_response):
        self.get_response = get_response
        self.backend_urls = (
            '/backend/',
            '/backend/dashboard',
            '/backend/blogs',
            '/backend/blogs/edit',
            '/backend/blogs/add',
            '/backend/blogs/update',
            '/backend/blogs/delete',
            '/backend/categories',
            '/backend/categories/new',
            '/backend/categories/delete',
            '/backend/author',
            '/backend/author/update',
            '/backend/password/edit',
            '/backend/password/update',
            '/backend/config/edit',
            '/backend/config/update',
            '/backend/tools',
            '/backend/tools/generate',
            '/backend/statistics',
            '/backend/statistics/blog_query',
            '/backend/statistics/access_query',
            '/backend/dologout',
        )
        self.except_urls = (
            '/backend/login',
            '/backend/dologin',
            '/backend/install',
            '/backend/install/init'
        )

    def __call__(self, request):
        # 加载配置
        if request.path in self.backend_urls and request.session['conf']['conf_site_auth'] == 'backend-only':
            # 仅后台拦截
            if 'user' not in request.session:
                return HttpResponseRedirect('/backend/login')
        elif request.path not in self.except_urls and request.session['conf']['conf_site_auth'] == 'all':
            # 全站拦截
            if 'user' not in request.session:
                return HttpResponseRedirect('/backend/login')
        response = self.get_response(request)
        return response

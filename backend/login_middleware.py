from django.http import HttpResponseRedirect
from blog.models import Conf


class LoginMiddleware:
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
            '/backend/statistics',
            '/backend/statistics/blog_query',
            '/backend/statistics/access_query',
            '/backend/dologout',
        )
        self.except_urls = (
            '/backend/login',
            '/backend/dologin',
        )

    def __call__(self, request):
        # 配置不存在就加入session
        if 'conf' not in request.session:
            conf1 = Conf.objects.filter(conf_key='conf_site_auth').first()
            conf2 = Conf.objects.filter(conf_key='conf_statistics').first()
            if conf1 is None:
                conf1 = Conf(conf_key='conf_site_auth',
                             conf_value='backend-only')
                conf1.save()
            if conf2 is None:
                conf2 = Conf(conf_key='conf_statistics', conf_value='close')
                conf2.save()
            request.session['conf'] = {
                'conf_site_auth': conf1.conf_value,
                'conf_statistics': conf2.conf_value
            }
        # 加载配置
        if request.session['conf']['conf_site_auth'] == 'backend-only':
            # 仅后台拦截
            if request.path in self.backend_urls:
                if 'user' not in request.session:
                    return HttpResponseRedirect('/backend/login')
        elif request.session['conf']['conf_site_auth'] == 'all':
            # 全站拦截
            if request.path not in self.except_urls:
                if 'user' not in request.session:
                    return HttpResponseRedirect('/backend/login')
        response = self.get_response(request)
        return response

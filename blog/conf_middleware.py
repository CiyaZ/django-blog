"""配置初始化拦截器
请求处理前，确保站点配置载入session，
清除处理过程中配置统一从session中取用，
Django默认使用数据库保存session，因此这样做没有任何性能优势，
但是如果改为采用缓存组件，会有较大性能提升
"""
from django.http import HttpResponseRedirect
from blog.models import Conf, BlogUser


class ConfMiddleware:
    """配置拦截器"""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.path.startswith('/backend/install'):
            # 如果数据库尚未初始化，直接跳到/backend/install
            blog_user = BlogUser.objects.filter(id=1).first()
            if blog_user is None:
                return HttpResponseRedirect('/backend/install')

            # 如果配置信息在session中不存在，载入session
            if 'conf' not in request.session:
                conf1 = Conf.objects.filter(conf_key='conf_site_auth').first()
                conf2 = Conf.objects.filter(conf_key='conf_statistics').first()
                conf3 = Conf.objects.filter(conf_key='conf_domain').first()
                conf4 = Conf.objects.filter(conf_key='conf_protocol').first()
                conf5 = Conf.objects.filter(conf_key='conf_sitemap_trigger').first()
                request.session['conf'] = {
                    'conf_site_auth': conf1.conf_value,
                    'conf_statistics': conf2.conf_value,
                    'conf_domain': conf3.conf_value,
                    'conf_protocol': conf4.conf_value,
                    'conf_sitemap_trigger': conf5.conf_value
                }
            response = self.get_response(request)
            return response
        else:
            response = self.get_response(request)
            return response

"""站点后端请求数统计拦截器
用于统计站点后端请求数，对性能有一定影响，
该拦截器对应配置默认关闭
"""
from django.utils.timezone import now
from blog.models import AccessLog


class StatisticsMiddleware:
    """访问统计日志拦截器"""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.path.startswith('/backend/install'):
            conf = request.session['conf']['conf_statistics']
            if conf == 'open':
                url = request.get_full_path()
                user_agent = request.META['HTTP_USER_AGENT']
                if len(url) > 255:
                    url = url[0:255]
                if len(user_agent) > 255:
                    user_agent = user_agent[0:255]
                log = AccessLog(url=url, user_agent=user_agent,
                                access_time=now())
                log.save()
            response = self.get_response(request)
            return response
        else:
            response = self.get_response(request)
            return response

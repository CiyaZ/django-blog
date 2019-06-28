from blog.models import AccessLog, Conf
from django.utils.timezone import now


class StatisticsMiddleware:
    """访问统计日志拦截器"""
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        conf = Conf.objects.filter(conf_key='conf_statistics').first()
        if conf is None:
            conf = Conf(conf_key='conf_statistics', conf_value='close')
            conf.save()
        if conf.conf_value == 'open':
            url = request.get_full_path()
            user_agent = request.META['HTTP_USER_AGENT']
            if len(url) > 255:
                url = url[0:255]
            if len(user_agent) > 255:
                user_agent = user_agent[0:255]
            log = AccessLog(url=url, user_agent=user_agent, access_time=now())
            log.save()
        response = self.get_response(request)
        return response

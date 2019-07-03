"""站点配置
修改数据库中站点配置信息
"""
from django.shortcuts import render
from django.http import HttpResponseBadRequest
from blog.models import Conf


def site_config_edit(request):
    """站点设置页"""
    conf_site_auth = request.session['conf']['conf_site_auth']
    conf_statistics = request.session['conf']['conf_statistics']
    conf_protocol = request.session['conf']['conf_protocol']
    conf_domain = request.session['conf']['conf_domain']

    return render(request, 'site_config.html', {
        'conf_site_auth': conf_site_auth,
        'conf_statistics': conf_statistics,
        'conf_protocol': conf_protocol,
        'conf_domain': conf_domain
    })


def site_config_update(request):
    """站点设置更新"""
    conf_site_auth = request.POST.get('conf_site_auth')
    conf_statistics = request.POST.get('conf_statistics')
    conf_protocol = request.POST.get('conf_protocol')
    conf_domain = request.POST.get('conf_domain')

    # 非法提交
    if conf_site_auth not in ('backend-only', 'all'):
        return HttpResponseBadRequest("Http 400 Bad Request")
    if conf_statistics not in ('open', 'close'):
        return HttpResponseBadRequest("Http 400 Bad Request")
    if conf_protocol not in ('http', 'https'):
        return HttpResponseBadRequest("Http 400 Bad Request")
    if conf_domain is None or conf_domain == '' or len(conf_domain) > 255:
        return HttpResponseBadRequest("Http 400 Bad Request")

    # 保存配置到数据库
    conf1 = Conf.objects.filter(conf_key='conf_site_auth').first()
    conf1.conf_value = conf_site_auth
    conf1.save()
    conf2 = Conf.objects.filter(conf_key='conf_statistics').first()
    conf2.conf_value = conf_statistics
    conf2.save()
    conf3 = Conf.objects.filter(conf_key='conf_protocol').first()
    conf3.conf_value = conf_protocol
    conf3.save()
    conf4 = Conf.objects.filter(conf_key='conf_domain').first()
    conf4.conf_value = conf_domain
    conf4.save()

    # 刷新session中的配置
    conf1 = Conf.objects.filter(conf_key='conf_site_auth').first()
    conf2 = Conf.objects.filter(conf_key='conf_statistics').first()
    conf3 = Conf.objects.filter(conf_key='conf_domain').first()
    conf4 = Conf.objects.filter(conf_key='conf_protocol').first()
    request.session['conf'] = {
        'conf_site_auth': conf1.conf_value,
        'conf_statistics': conf2.conf_value,
        'conf_domain': conf3.conf_value,
        'conf_protocol': conf4.conf_value
    }

    return render(request, 'site_config.html', {
        'status': 'success',
        'conf_site_auth': conf_site_auth,
        'conf_statistics': conf_statistics,
        'conf_protocol': conf_protocol,
        'conf_domain': conf_domain
    })

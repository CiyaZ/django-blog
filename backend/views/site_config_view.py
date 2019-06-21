from django.shortcuts import render
from django.http import HttpResponseBadRequest
from blog.models import Conf


def site_config_edit(request):
    """站点设置页"""
    conf1 = Conf.objects.filter(conf_key='conf_site_auth').first()
    conf2 = Conf.objects.filter(conf_key='conf_statistics').first()

    conf_site_auth = 'backend-only'
    conf_statistics = 'close'
    if conf1 is not None:
        conf_site_auth = conf1.conf_value
    if conf2 is not None:
        conf_statistics = conf2.conf_value

    return render(request, 'site_config.html', {
        'conf_site_auth': conf_site_auth,
        'conf_statistics': conf_statistics
    })


def site_config_update(request):
    """站点设置更新"""
    conf_site_auth = request.POST.get('conf_site_auth')
    conf_statistics = request.POST.get('conf_statistics')

    # 非法提交
    if conf_site_auth not in ('backend-only', 'all'):
        return HttpResponseBadRequest("Http 400 Bad Request")
    if conf_statistics not in ('open', 'close'):
        return HttpResponseBadRequest("Http 400 Bad Request")

    # 保存配置
    conf1 = Conf.objects.filter(conf_key='conf_site_auth').first()
    if conf1 is None:
        conf1 = Conf(conf_key='conf_site_auth', conf_value=conf_site_auth)
    else:
        conf1.conf_value = conf_site_auth
    conf1.save()

    conf2 = Conf.objects.filter(conf_key='conf_statistics').first()
    if conf2 is None:
        conf2 = Conf(conf_key='conf_statistics', conf_value=conf_statistics)
    else:
        conf2.conf_value = conf_statistics
    conf2.save()

    request.session['conf'] = {
        'conf_site_auth': conf1.conf_value,
        'conf_statistics': conf2.conf_value
    }

    return render(request, 'site_config.html', {
        'status': 'success',
        'conf_site_auth': conf_site_auth,
        'conf_statistics': conf_statistics
    })

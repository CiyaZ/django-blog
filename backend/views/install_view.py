"""表初始化
第一次运行时执行初始化操作，
插入用户、初始文章和分类，并初始化配置
"""
import re
from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from django.utils.timezone import now
from blog.models import BlogUser, Category, Blog, Conf


def install(request):
    """初始化用户页面"""
    blog_user = BlogUser.objects.filter(id=1).first()
    if blog_user is None:
        return render(request, 'install.html')
    else:
        # 已初始化不允许再次访问
        return HttpResponseRedirect('/index')
    

def do_install(request):
    """执行用户初始化"""
    # 已初始化不允许再次访问
    blog_user = BlogUser.objects.filter(id=1).first()
    if blog_user is not None:
        return HttpResponseRedirect('/index')

    # 取表单字段
    protocol = request.POST.get('protocol')
    domain = request.POST.get('domain')
    username = request.POST.get('username')
    email = request.POST.get('email')
    avatar = request.POST.get('avatar')
    motto = request.POST.get('motto')
    password = request.POST.get('password')

    # 非法提交校验
    if protocol != 'http' and protocol != 'https':
        return HttpResponseBadRequest("Http 400 Bad Request")
    if domain is None or domain == '' or len(domain) > 255:
        return HttpResponseBadRequest("Http 400 Bad Request")
    if username is None or username == '' or len(username) > 20 or re.match('^[0-9a-zA-Z]+$', username) is None:
        return HttpResponseBadRequest("Http 400 Bad Request")
    if email is not None and email != '':
        if email == '' or len(email) > 255:
            return HttpResponseBadRequest("Http 400 Bad Request")
    else:
        email = None
    if avatar is not None and avatar != '':
        if avatar == '' or len(avatar) > 255:
            return HttpResponseBadRequest("Http 400 Bad Request")
    else:
        avatar = None
    if motto is not None and motto != '':
        if motto == '' or len(motto) > 255:
            return HttpResponseBadRequest("Http 400 Bad Request")
    else:
        motto = None
    if password == '' or len(password) > 255:
        return HttpResponseBadRequest("Http 400 Bad Request")

    # 初始用户插入
    blog_user = BlogUser(
        pk=1,
        username=username,
        email=email,
        avatar=avatar,
        motto=motto,
        password=make_password(password)
    )
    blog_user.save()

    # 初始分类和文章插入
    category = Category(category_name='测试分类')
    category.save()
    blog = Blog(
        title='Hello, world!',
        content='这是一篇默认文章，你可以将其删除，开始你的创作',
        content_rendered='<p>这是一篇默认文章，你可以将其删除，开始你的创作</p>',
        content_abstract='这是一篇默认文章，你可以将其删除，开始你的创作',
        category=category,
        create_time=now(),
        last_modified_time=now())
    blog.save()

    # 初始配置插入
    conf1 = Conf(conf_key='conf_site_auth', conf_value='backend-only')
    conf2 = Conf(conf_key='conf_statistics', conf_value='close')
    conf3 = Conf(conf_key='conf_domain', conf_value=domain)
    conf4 = Conf(conf_key='conf_protocol', conf_value=protocol)
    conf5 = Conf(conf_key='conf_sitemap_trigger', conf_value='open')
    conf6 = Conf(conf_key='conf_reply_enabled', conf_value='open')
    conf7 = Conf(conf_key='conf_reply_precheck', conf_value='open')
    conf1.save()
    conf2.save()
    conf3.save()
    conf4.save()
    conf5.save()
    conf6.save()
    conf7.save()

    return HttpResponseRedirect('/index')

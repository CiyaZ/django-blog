import re
from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from django.utils.timezone import now
from blog.models import BlogUser, Category, Blog


def install(request):
    """初始化用户页面"""
    return render(request, 'install.html')


def do_install(request):
    """执行用户初始化"""
    username = request.POST.get('username')
    email = request.POST.get('email')
    avatar = request.POST.get('avatar')
    motto = request.POST.get('motto')
    password = request.POST.get('password')

    # 非法提交校验
    if username is None or len(username) < 1 or len(username) > 20 or re.match('^[0-9a-zA-Z]+$', username) is None:
        return HttpResponseBadRequest("Http 400 Bad Request")
    if email is not None and email != '':
        if len(email) < 1 or len(email) > 255:
            return HttpResponseBadRequest("Http 400 Bad Request")
    else:
        email = None
    if avatar is not None and avatar != '':
        if len(avatar) < 1 or len(avatar) > 255:
            return HttpResponseBadRequest("Http 400 Bad Request")
    else:
        avatar = None
    if motto is not None and motto != '':
        if len(motto) < 1 or len(motto) > 255:
            return HttpResponseBadRequest("Http 400 Bad Request")
    else:
        motto = None
    if len(password) < 1 or len(password) > 255:
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
        create_time=now())
    blog.save()

    return HttpResponseRedirect('/index')

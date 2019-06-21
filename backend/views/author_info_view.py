from django.shortcuts import render
from django.http import HttpResponseBadRequest
from blog.models import BlogUser
import re


def author_info(request):
    """显示博主信息编辑页"""
    blog_user = BlogUser.objects.get(id=1)
    return render(request, 'author_info.html', {
        'blog_user': blog_user
    })


def author_info_update(request):
    """更新博主信息"""
    username = request.POST.get('username')
    email = request.POST.get('email')
    avatar = request.POST.get('avatar')
    motto = request.POST.get('motto')

    # 非法提交
    if username is None or len(username) < 1 or len(username) > 20 or re.match('^[0-9a-zA-Z]+$', username) is None:
        return HttpResponseBadRequest()
    if email is not None:
        if len(email) < 1 or len(email) > 255:
            return HttpResponseBadRequest()
    if avatar is not None:
        if len(avatar) < 1 or len(avatar) > 255:
            return HttpResponseBadRequest()
    if motto is not None:
        if len(motto) < 1 or len(motto) > 255:
            return HttpResponseBadRequest()

    # 更新
    blog_user = BlogUser.objects.get(id=1)
    if username is not None:
        blog_user.username = username
    if email is not None:
        blog_user.email = email
    if avatar is not None:
        blog_user.avatar = avatar
    if motto is not None:
        blog_user.motto = motto
    blog_user.save()

    return render(request, 'author_info.html', {
        'blog_user': blog_user,
        'msg': 'success'
    })

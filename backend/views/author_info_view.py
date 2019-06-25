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
    if email is not None and email != '':
        if len(email) < 1 or len(email) > 255:
            return HttpResponseBadRequest()
    else:
        email = None
    if avatar is not None and avatar != '':
        if len(avatar) < 1 or len(avatar) > 255:
            return HttpResponseBadRequest()
    else:
        avatar = None
    if motto is not None and motto != '':
        if len(motto) < 1 or len(motto) > 255:
            return HttpResponseBadRequest()
    else:
        motto = None

    print(username)
    print(email)
    print(avatar)
    print(motto)

    # 更新
    blog_user = BlogUser.objects.get(id=1)
    if username is not None:
        blog_user.username = username
    blog_user.email = email
    blog_user.avatar = avatar
    blog_user.motto = motto
    blog_user.save()

    return render(request, 'author_info.html', {
        'blog_user': blog_user,
        'msg': 'success'
    })

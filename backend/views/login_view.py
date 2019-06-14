from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.contrib.auth.hashers import make_password, check_password
from blog.models import BlogUser


def login(request):
    blog_user = BlogUser.objects.get(id=1)
    return render(request, 'login.html', {
        'blog_user': blog_user
    })


def do_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    # 非法提交
    if len(username) < 1 or len(username) > 20:
        return HttpResponseBadRequest("Http 400 Bad Request")

    if len(password) < 1 or len(password) > 255:
        return HttpResponseBadRequest("Http 400 Bad Request")

    # 身份认证
    blog_user = BlogUser.objects.get(id=1)
    if username == blog_user.username and check_password(password, blog_user.password):
        # 登录成功
        blog_user_session = {
            'username': blog_user.username,
            'email': blog_user.email,
            'avatar': blog_user.avatar,
            'motto': blog_user.motto
        }
        request.session['user'] = blog_user_session
        return HttpResponseRedirect('/backend/dashboard')
    else:
        # 登录失败
        return render(request, 'login.html', {
            'error': True,
            'msg': '用户名或密码错误'
        })


def do_logout(request):
    request.session.pop('user')
    return HttpResponseRedirect('/backend/login')
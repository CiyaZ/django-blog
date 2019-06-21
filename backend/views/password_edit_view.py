from django.shortcuts import render
from django.http import HttpResponseBadRequest
from django.contrib.auth.hashers import make_password, check_password
from blog.models import BlogUser


def password_edit(request):
    """获取密码修改页"""
    return render(request, 'password_edit.html')


def password_update(request):
    """更新密码"""
    password = request.POST.get('password')
    new_password = request.POST.get('newpassword')
    re_password = request.POST.get('repassword')

    # 非法提交
    if len(password) < 1 or len(password) > 255:
        return HttpResponseBadRequest("Http 400 Bad Request")
    if len(new_password) < 1 or len(new_password) > 255:
        return HttpResponseBadRequest("Http 400 Bad Request")
    if len(re_password) < 1 or len(re_password) > 255:
        return HttpResponseBadRequest("Http 400 Bad Request")

    # 原密码检查
    blog_user = BlogUser.objects.get(id=1)
    if check_password(password, blog_user.password):
        new_password_enc = make_password(new_password)
        blog_user.password = new_password_enc
        blog_user.save()
        return render(request, 'password_edit.html', {
            'status': 'success',
            'msg': '修改成功'
        })
    else:
        return render(request, 'password_edit.html', {
            'status': 'error',
            'msg': '原密码错误'
        })

from django.shortcuts import render
from blog.models import BlogUser


def dashboard(request):
    """获取后台框架主页"""
    blog_user = BlogUser.objects.get(id=1)
    return render(request, 'dashboard.html', {
        'blog_user': blog_user
    })

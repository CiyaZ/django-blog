from django.shortcuts import render
from django.core.paginator import Paginator
from ..models import BlogUser
from ..models import Blog
from ..models import Category


def blog(request, id):
    # 当前用户
    blog_user = BlogUser.objects.get(id=1)
    # 当前文章
    blog = Blog.objects.get(id=id)

    return render(request, 'blog.html', {
        'blog_user': blog_user,
        'blog': blog
    })

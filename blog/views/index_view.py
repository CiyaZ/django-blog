from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect

from blog.utils.page_util import calc_page_btn_list
from blog.models import BlogUser
from blog.models import Blog
from blog.models import Category
from blog.models import Link


def index(request):
    """首页"""
    # 分页和分类查询参数
    current_page = request.GET.get('page')
    if current_page is None:
        current_page = 1
    else:
        current_page = int(current_page)
    page_size = request.GET.get('size')
    if page_size is None or int(page_size) > 20:
        page_size = 20
    else:
        page_size = int(page_size)
    category_id = request.GET.get('category')
    pattern = request.GET.get('pattern')

    # 当前用户
    blog_user = BlogUser.objects.filter(id=1).first()
    if blog_user is None:
        return HttpResponseRedirect('/backend/install')

    # 分类
    category_list = Category.objects.all()
    category = None
    if category_id is not None:
        category = Category.objects.get(id=category_id)

    # 友情链接
    link_list = Link.objects.all()

    # 分页动态查询文章
    blog_list = Blog.objects.all()
    if pattern is not None and pattern != '':
        blog_list = blog_list.filter(
            content__contains=pattern) | blog_list.filter(title__contains=pattern)
    if category_id is not None:
        blog_list = blog_list.filter(category_id=category_id)
    blog_list = blog_list.order_by('-create_time')
    paginator = Paginator(blog_list, page_size)
    blog_list_page = paginator.page(current_page)

    # 分页按钮组计算
    page_btn_list = calc_page_btn_list(paginator, current_page)

    return render(request, 'index.html', {
        'blog_user': blog_user,
        'blog_list_page': blog_list_page,
        'category_list': category_list,
        'page_btn_list': page_btn_list,
        'link_list': link_list,
        'category_id': category_id,
        'category': category,
        'current_page': current_page,
        'page_size': page_size,
        'pattern': pattern
    })

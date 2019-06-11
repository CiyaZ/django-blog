from django.shortcuts import render
from django.core.paginator import Paginator
from ..models import BlogUser
from ..models import Blog
from ..models import Category


def index(request):
    # 分页和分类查询参数
    current_page = request.GET.get('page')
    if current_page == None:
        current_page = 1
    else:
        current_page = int(current_page)
    page_size = request.GET.get('size')
    if page_size == None or int(page_size) > 20:
        page_size = 20
    else:
        page_size = int(page_size)
    category_id = request.GET.get('category')

    # 当前用户
    blog_user = BlogUser.objects.get(id=1)

    # 分类
    category_list = Category.objects.all()
    category = None
    if category_id != None:
        category = Category.objects.get(id=category_id)

    # 分页动态查询文章
    blog_list = Blog.objects.all()
    if category_id != None:
        blog_list = blog_list.filter(category_id=category_id)
    blog_list = blog_list.order_by('-create_time')
    paginator = Paginator(blog_list, page_size)
    blog_list_page = paginator.page(current_page)

    # 分页按钮组计算
    page_btn_list = []
    offset = 0
    print(paginator.page_range)
    if current_page - 2 in paginator.page_range:
        page_btn_list.append(current_page - 2)
    else:
        offset += 1
    if current_page - 1 in paginator.page_range:
        page_btn_list.append(current_page - 1)
    else:
        offset += 1
    page_btn_list.append(current_page)
    if current_page + 1 in paginator.page_range:
        page_btn_list.append(current_page + 1)
    if current_page + 2 in paginator.page_range:
        page_btn_list.append(current_page + 2)
    for i in range(1, offset + 1):
        if current_page + 2 + i in paginator.page_range:
            page_btn_list.append(current_page + 2 + i)

    return render(request, 'index.html', {
        'blog_user': blog_user,
        'blog_list_page': blog_list_page,
        'category_list': category_list,
        'page_btn_list': page_btn_list,
        'category_id': category_id,
        'category': category,
        'current_page': current_page,
        'page_size': page_size
    })

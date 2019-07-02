from django.shortcuts import render
from django.core.paginator import Paginator
from django.utils.timezone import now
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest, JsonResponse
import markdown
import re
from blog.models import Blog, Category


def blog_list(request):
    """博文列表页"""
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

    # 分类
    category_list = Category.objects.all()
    category = None
    if category_id is not None and category_id != 'all':
        category = Category.objects.get(id=category_id)
    # 分页动态查询文章
    blog_list = Blog.objects.all()
    if pattern is not None and pattern != '':
        blog_list = blog_list.filter(
            content__contains=pattern) | blog_list.filter(title__contains=pattern)
    if category_id is not None and category_id != 'all':
        blog_list = blog_list.filter(category_id=category_id)
    blog_list = blog_list.order_by('-create_time')
    paginator = Paginator(blog_list, page_size)
    blog_list_page = paginator.page(current_page)

    # 分页按钮组计算
    page_btn_list = []
    offset = 0
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

    return render(request, 'blog_list.html', {
        'blog_list_page': blog_list_page,
        'category_list': category_list,
        'page_btn_list': page_btn_list,
        'category_id': category_id,
        'category': category,
        'current_page': current_page,
        'page_size': page_size,
        'pattern': pattern
    })


def delete_blog(request):
    """删除文章"""
    id = request.GET.get('id')
    if id is not None:
        Blog.objects.get(pk=id).delete()
    return HttpResponseRedirect('/backend/blogs')


def edit_blog(request):
    """编辑文章页面，如果是更新，回显文章Markdown源码到表单"""
    id = request.GET.get('id')
    blog = None
    if id != None:
        blog = Blog.objects.get(id=id)

    action = 'add'
    if blog != None:
        action = 'update'

    category_list = Category.objects.all()
    return render(request, 'blog_edit.html', {
        'action': action,
        'blog': blog,
        'category_list': category_list
    })


def add_blog(request):
    """创建文章"""
    title = request.POST.get('title')
    category_id = request.POST.get('category')
    content = request.POST.get('content')
    category = None

    # 非法提交
    if title is None or len(title) < 1 or len(title) > 100:
        return HttpResponseBadRequest("Http 400 Bad Request")
    if content is None or len(content) < 1 or len(content) > 20000:
        return HttpResponseBadRequest("Http 400 Bad Request")
    if category_id is None or category_id == '':
        return HttpResponseBadRequest("Http 400 Bad Request")
    else:
        category = Category.objects.get(id=category_id)

    content_rendered, content_abstract, content_img1, content_img2, content_img3 = blog_content_calc(content)

    if category is not None:
        blog = Blog(
            title=title,
            content=content,
            content_rendered=content_rendered,
            content_abstract=content_abstract,
            content_img1=content_img1,
            content_img2=content_img2,
            content_img3=content_img3,
            category=category,
            create_time=now(),
            last_modified_time=now())
        blog.save()
        return JsonResponse({
            'id': blog.pk
        })

    return HttpResponse()


def update_blog(request):
    """更新文章"""
    blog_id = request.POST.get('id')
    title = request.POST.get('title')
    category_id = request.POST.get('category')
    content = request.POST.get('content')
    blog = None
    category = None

    # 非法提交
    if title is None or len(title) < 1 or len(title) > 100:
        return HttpResponseBadRequest("Http 400 Bad Request")
    if content is None or len(content) < 1 or len(content) > 20000:
        return HttpResponseBadRequest("Http 400 Bad Request")
    if category_id is None or category_id == '':
        return HttpResponseBadRequest("Http 400 Bad Request")
    else:
        category = Category.objects.get(id=category_id)
        blog = Blog.objects.get(id=blog_id)

    content_rendered, content_abstract, content_img1, content_img2, content_img3 = blog_content_calc(content)

    if category is not None and blog is not None:
        blog.title = title
        blog.content = content
        blog.content_rendered = content_rendered
        blog.content_abstract = content_abstract
        blog.content_img1 = content_img1
        blog.content_img2 = content_img2
        blog.content_img3 = content_img3
        blog.category = category
        blog.last_modified_time = now()
        blog.save()

    return HttpResponse()


def blog_content_calc(content):
    """markdown渲染，识别文章摘要，识别文章中图片"""
    content_rendered = markdown.markdown(content, extensions=['markdown.extensions.extra', 'markdown.extensions.codehilite', 'markdown.extensions.tables'])

    content_abstract = None
    content_lines = content.split('\n')
    for line in content_lines:
        if not line.startswith('#') and line.strip() != '':
            content_abstract = line
            break

    content_imgs = []
    for line in content_lines:
        match = re.match(r'\!\[\]\((.*)\)', line)
        if match:
            content_imgs.append(match.group(1))
    content_img1 = None
    content_img2 = None
    content_img3 = None
    if len(content_imgs) >= 1:
        content_img1 = content_imgs[0]
    if len(content_imgs) >= 2:
        content_img2 = content_imgs[1]
    if len(content_imgs) >= 3:
        content_img3 = content_imgs[2]

    return (content_rendered, content_abstract, content_img1, content_img2, content_img3)

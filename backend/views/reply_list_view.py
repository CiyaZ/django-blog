"""评论管理控制器
"""
from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect

from blog.models import Reply


def reply_list(request):
    """评论后台管理分页"""
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

    # 评论分页查询
    reply_list = Reply.objects.all().order_by('-create_time')
    paginator = Paginator(reply_list, page_size)
    reply_list_page = paginator.page(current_page)

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

    return render(request, 'reply_list.html', {
        'reply_list_page': reply_list_page,
        'page_btn_list': page_btn_list,
        'current_page': current_page,
        'page_size': page_size
    })


def delete_reply(request):
    """删除评论"""
    reply_id = request.GET.get('id')
    if reply_id is not None:
        Reply.objects.get(pk=reply_id).delete()

    return HttpResponseRedirect('/backend/replies')

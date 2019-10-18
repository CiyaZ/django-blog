from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse, HttpResponseBadRequest
from django.utils.timezone import now
import hashlib
from ..models import BlogUser
from ..models import Blog
from ..models import Reply


def blog(request, id):
    """文章页面"""
    # 当前用户
    blog_user = BlogUser.objects.get(id=1)
    # 当前文章
    blog = Blog.objects.get(id=id)
    # 评论信息
    replies = Reply.objects.filter(blog_id=id, root_reply_id=None)

    return render(request, 'blog.html', {
        'blog_user': blog_user,
        'blog': blog,
        'replies': replies
    })


def add_reply(request):
    """发表评论"""
    conf_reply_enabled = request.session['conf']['conf_reply_enabled']
    if conf_reply_enabled == 'open':
        nickname = request.POST.get('nickname')
        email = request.POST.get('email')
        url = request.POST.get('url')
        content = request.POST.get('content')
        blog_id = request.POST.get('blogId')
        parent_reply_id = request.POST.get('parentReplyId')
        root_reply_id = request.POST.get('rootReplyId')

        # 非法提交
        if nickname is None or len(nickname) < 1 or len(nickname) > 20:
            return HttpResponseBadRequest("Http 400 Bad Request")
        if email is None or len(email) < 1 or len(email) > 50:
            return HttpResponseBadRequest("Http 400 Bad Request")
        if len(url) > 255:
            return HttpResponseBadRequest("Http 400 Bad Request")
        if content is None or len(content) < 1 or len(content) > 1000:
            return HttpResponseBadRequest("Http 400 Bad Request")

        if parent_reply_id == '':
            parent_reply_id = None
        if root_reply_id == '':
            root_reply_id = None

        floor_index = 0
        if root_reply_id is None:
            ref_blog = Blog.objects.get(id=blog_id)
            floor_index = ref_blog.floors + 1
            ref_blog.floors = floor_index
            ref_blog.save()

        reply = Reply(nickname=nickname, email=email, url=url, content=content, blog_id=blog_id,
                      parent_reply_id=parent_reply_id, root_reply_id=root_reply_id, floor_index=floor_index,
                      create_time=now())
        reply.save()

        return HttpResponseRedirect('/blogs/' + blog_id)
    else:
        return HttpResponseRedirect('/index')


def load_sub_replies(request):
    """异步加载二级评论"""
    conf_reply_enabled = request.session['conf']['conf_reply_enabled']
    if conf_reply_enabled == 'open':
        root_reply_id = request.GET.get('replyId')
        if root_reply_id is None or root_reply_id == '':
            return JsonResponse({})
        replies = Reply.objects.filter(root_reply_id=root_reply_id)

        result_json = {'data': []}
        for reply in replies:
            email = reply.email
            gravatar_url = 'https://s.gravatar.com/avatar/' + \
                           hashlib.md5(email.lower().encode('utf8')).hexdigest() + \
                           '?s=' + str(40)

            result_json['data'].append({
                'id': reply.id,
                'nickname': reply.nickname,
                'gravatarUrl': gravatar_url,
                'url': reply.url,
                'content': reply.content,
                'blogId': reply.blog_id,
                'parentReplyId': reply.parent_reply_id,
                'rootReplyId': reply.root_reply_id,
                'createTime': reply.create_time.strftime("%Y-%m-%d %H:%M:%S")
            })
        return JsonResponse(result_json, json_dumps_params={'ensure_ascii': False})
    else:
        return JsonResponse({})

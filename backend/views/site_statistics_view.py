"""站点统计功能
包括文章发布数量统计和后端请求数统计，
用于提醒站点拥有者文章的内容的发布频率和站点性能
"""
from datetime import datetime, timedelta
from django.shortcuts import render
from django.http import JsonResponse
from django.utils.timezone import now
from blog.models import Blog, Category, AccessLog


def site_statistics(request):
    """站点统计页面"""
    # 该配置用于判断站点访问统计是否开启
    conf_statistics = request.session['conf']['conf_statistics']
    return render(request, 'site_statistics.html', {
        'conf': conf_statistics
    })


def blog_statistics_query(request):
    """文章量统计"""
    # 文章总数
    blogs_cnt = Blog.objects.count()
    # 分类总数
    category_cnt = Category.objects.count()
    # 过去7天每天的文章发布数
    datetime_now = now()
    datetime_year = datetime_now.year
    datetime_month = datetime_now.month
    datetime_day = datetime_now.day
    datetime_negtive0 = datetime(datetime_year, datetime_month, datetime_day)
    datetime_positive1 = datetime_negtive0 + timedelta(days=1)
    datetime_negtive1 = datetime_negtive0 - timedelta(days=1)
    datetime_negtive2 = datetime_negtive0 - timedelta(days=2)
    datetime_negtive3 = datetime_negtive0 - timedelta(days=3)
    datetime_negtive4 = datetime_negtive0 - timedelta(days=4)
    datetime_negtive5 = datetime_negtive0 - timedelta(days=5)
    datetime_negtive6 = datetime_negtive0 - timedelta(days=6)
    cnt1 = Blog.objects.filter(
        create_time__gte=datetime_negtive0, create_time__lte=datetime_positive1).count()
    cnt2 = Blog.objects.filter(
        create_time__gte=datetime_negtive1, create_time__lte=datetime_negtive0).count()
    cnt3 = Blog.objects.filter(
        create_time__gte=datetime_negtive2, create_time__lte=datetime_negtive1).count()
    cnt4 = Blog.objects.filter(
        create_time__gte=datetime_negtive3, create_time__lte=datetime_negtive2).count()
    cnt5 = Blog.objects.filter(
        create_time__gte=datetime_negtive4, create_time__lte=datetime_negtive3).count()
    cnt6 = Blog.objects.filter(
        create_time__gte=datetime_negtive5, create_time__lte=datetime_negtive4).count()
    cnt7 = Blog.objects.filter(
        create_time__gte=datetime_negtive6, create_time__lte=datetime_negtive5).count()
    result_cnt = [
        {
            'date': '{0}月{1}日'.format(datetime_negtive6.month, datetime_negtive6.day),
            'value': cnt7
        },
        {
            'date': '{0}月{1}日'.format(datetime_negtive5.month, datetime_negtive5.day),
            'value': cnt6
        },
        {
            'date': '{0}月{1}日'.format(datetime_negtive4.month, datetime_negtive4.day),
            'value': cnt5
        },
        {
            'date': '{0}月{1}日'.format(datetime_negtive3.month, datetime_negtive3.day),
            'value': cnt4
        },
        {
            'date': '{0}月{1}日'.format(datetime_negtive2.month, datetime_negtive2.day),
            'value': cnt3
        },
        {
            'date': '{0}月{1}日'.format(datetime_negtive1.month, datetime_negtive1.day),
            'value': cnt2
        },
        {
            'date': '{0}月{1}日'.format(datetime_negtive0.month, datetime_negtive0.day),
            'value': cnt1
        },
    ]
    # 返回JSON
    return JsonResponse({
        'blog_cnt': blogs_cnt,
        'category_cnt': category_cnt,
        'blogs_cnt': result_cnt
    })


def access_statistics_query(request):
    """后端请求统计"""
    datetime_now = now()
    datetime_year = datetime_now.year
    datetime_month = datetime_now.month
    datetime_day = datetime_now.day
    datetime_negtive0 = datetime(datetime_year, datetime_month, datetime_day)
    datetime_positive1 = datetime_negtive0 + timedelta(days=1)
    datetime_negtive1 = datetime_negtive0 - timedelta(days=1)
    datetime_negtive2 = datetime_negtive0 - timedelta(days=2)
    datetime_negtive3 = datetime_negtive0 - timedelta(days=3)
    datetime_negtive4 = datetime_negtive0 - timedelta(days=4)
    datetime_negtive5 = datetime_negtive0 - timedelta(days=5)
    datetime_negtive6 = datetime_negtive0 - timedelta(days=6)
    # 今日后端请求总量
    access_cnt = AccessLog.objects.filter(
        access_time__gte=datetime_negtive0, access_time__lte=datetime_positive1).count()
    # 过去7天后端请求量
    cnt1 = AccessLog.objects.filter(
        access_time__gte=datetime_negtive0, access_time__lte=datetime_positive1).count()
    cnt2 = AccessLog.objects.filter(
        access_time__gte=datetime_negtive1, access_time__lte=datetime_negtive0).count()
    cnt3 = AccessLog.objects.filter(
        access_time__gte=datetime_negtive2, access_time__lte=datetime_negtive1).count()
    cnt4 = AccessLog.objects.filter(
        access_time__gte=datetime_negtive3, access_time__lte=datetime_negtive2).count()
    cnt5 = AccessLog.objects.filter(
        access_time__gte=datetime_negtive4, access_time__lte=datetime_negtive3).count()
    cnt6 = AccessLog.objects.filter(
        access_time__gte=datetime_negtive5, access_time__lte=datetime_negtive4).count()
    cnt7 = AccessLog.objects.filter(
        access_time__gte=datetime_negtive6, access_time__lte=datetime_negtive5).count()
    result_cnt = [
        {
            'date': '{0}月{1}日'.format(datetime_negtive6.month, datetime_negtive6.day),
            'value': cnt7
        },
        {
            'date': '{0}月{1}日'.format(datetime_negtive5.month, datetime_negtive5.day),
            'value': cnt6
        },
        {
            'date': '{0}月{1}日'.format(datetime_negtive4.month, datetime_negtive4.day),
            'value': cnt5
        },
        {
            'date': '{0}月{1}日'.format(datetime_negtive3.month, datetime_negtive3.day),
            'value': cnt4
        },
        {
            'date': '{0}月{1}日'.format(datetime_negtive2.month, datetime_negtive2.day),
            'value': cnt3
        },
        {
            'date': '{0}月{1}日'.format(datetime_negtive1.month, datetime_negtive1.day),
            'value': cnt2
        },
        {
            'date': '{0}月{1}日'.format(datetime_negtive0.month, datetime_negtive0.day),
            'value': cnt1
        },
    ]
    # 返回JSON
    return JsonResponse({
        'access_cnt_today': access_cnt,
        'access_cnt': result_cnt
    })

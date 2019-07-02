from django.shortcuts import render
from django.http import HttpResponse
from backend.utils.sitemap_generator import generate_sitemap


def site_tools(request):
    """获取站点工具页面"""
    return render(request, 'site_tools.html')


def do_generate_sitemap(request):
    """刷新站点地图"""
    generate_sitemap()
    return HttpResponse()

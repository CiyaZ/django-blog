"""返回站点地图XML文件
站点地图保存在工程根目录sitemap.xml中
"""
from django.http import HttpResponse


def sitemap(request):
    """返回站点地图"""
    sitemap_file = open('sitemap.xml', 'r')
    sitemap_str = sitemap_file.read()
    sitemap_file.close()
    return HttpResponse(sitemap_str, content_type="application/xml")

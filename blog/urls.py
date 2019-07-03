"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from django.urls.conf import include
from blog.views.index_view import index
from blog.views.blog_view import blog
from blog.views.pages_view import about, help
from blog.views.sitemap_view import sitemap

urlpatterns = [
    path('', index),
    path('index', index),
    path('about', about),
    path('help', help),
    re_path(r'^blogs/(?P<id>[0-9]+)$', blog),
    path('backend/', include('backend.urls')),
    path('sitemap.xml', sitemap),
]

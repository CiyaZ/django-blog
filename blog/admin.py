from django.contrib import admin
from blog.models import BlogUser
from blog.models import Category
from blog.models import Blog
from blog.models import Link

admin.site.register(BlogUser)
admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(Link)

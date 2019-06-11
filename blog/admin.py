from django.contrib import admin
from .models import BlogUser
from .models import Category
from .models import Blog

admin.site.register(BlogUser)
admin.site.register(Category)
admin.site.register(Blog)

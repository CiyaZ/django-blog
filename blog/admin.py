from django.contrib import admin
from .models import BlogUser
from .models import Category
from .models import Blog
from .models import Link

admin.site.register(BlogUser)
admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(Link)

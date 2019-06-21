from django.db import models


class Conf(models.Model):
    """一些保存到数据库的运行时配置实体类"""
    conf_key = models.CharField(max_length=255)
    conf_value = models.CharField(max_length=255)


class BlogUser(models.Model):
    """backend后台用户实体类"""
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=255, null=True)
    password = models.CharField(max_length=255)
    avatar = models.CharField(max_length=255, null=True)
    motto = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.username


class Category(models.Model):
    """目录实体类"""
    category_name = models.CharField(max_length=20)

    def __str__(self):
        return self.category_name


class Blog(models.Model):
    """文章实体类"""
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=65535)
    content_rendered = models.TextField(max_length=65535, null=True)
    content_abstract = models.TextField(max_length=65535, null=True)
    content_img1 = models.CharField(max_length=255, null=True)
    content_img2 = models.CharField(max_length=255, null=True)
    content_img3 = models.CharField(max_length=255, null=True)
    create_time = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Link(models.Model):
    """友情链接实体类"""
    link_name = models.CharField(max_length=20)
    icon_src = models.CharField(max_length=255)
    link_href = models.CharField(max_length=255)

    def __str__(self):
        return self.link_name


class AccessLog(models.Model):
    """后端访问日志实体类"""
    url = models.CharField(max_length=255)
    user_agent = models.CharField(max_length=255)
    access_time = models.DateTimeField()

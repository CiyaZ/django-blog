from django.db import models


class BlogUser(models.Model):
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255)
    avatar = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.username


class Category(models.Model):
    category_name = models.CharField(max_length=20)

    def __str__(self):
        return self.category_name


class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=65535)
    create_time = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

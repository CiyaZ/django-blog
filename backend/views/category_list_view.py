from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from blog.models import Category


def category_list(request):
    """分类列表页"""
    category_list = Category.objects.all()

    return render(request, 'category_list.html', {
        'category_list': category_list
    })


def add_category(request):
    """添加分类"""
    category_name = request.POST.get('category_name')

    if category_name is None or len(category_name) < 1 or len(category_name) > 20:
        return HttpResponseBadRequest()

    category = Category(category_name=category_name)
    category.save()

    return HttpResponseRedirect('/backend/categories')


def delete_category(request):
    """删除分类"""
    id = request.GET.get('id')
    if id is not None:
        Category.objects.get(pk=id).delete()
    return HttpResponseRedirect('/backend/categories')

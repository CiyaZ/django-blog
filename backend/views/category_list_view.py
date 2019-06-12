from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from blog.models import Blog, Category


def category_list(request):

    category_list = Category.objects.all()

    return render(request, 'category_list.html', {
        'category_list': category_list
    })


def add_category(request):
    category_name = request.POST.get('category_name')

    if category_name == None or len(category_name) < 1 or len(category_name) > 20:
        return HttpResponseBadRequest()

    category = Category(category_name=category_name)
    category.save()

    return HttpResponseRedirect('/backend/categories')


def delete_category(request):
    id = request.GET.get('id')
    if id != None:
        Category.objects.get(pk=id).delete()
    return HttpResponseRedirect('/backend/categories')

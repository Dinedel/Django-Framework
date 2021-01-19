import json
import os
import random

from django.conf import settings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404

from .models import Product, ProductCategory


def get_hot_product():
    products = Product.objects.all()
    return random.sample(list(products), 1)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).\
        exclude(pk=hot_product.pk)[:3]
    return same_products


def main(request):
    #products = Product.objects.all()[:4]
    products = Product.objects.filter(is_active=True, category__is_active=True).\
                   select_related('category')[:3]

    content = {'title': 'Главная', 'products': products}
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None, page=1):
    print(pk)

    title = 'Продукты'
    links_menu = ProductCategory.objects.all()

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    if pk is not None:
        if int(pk) == 0:
            products_list = Product.objects.all()
            category = {'name': 'все', 'pk': 0}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products_list = Product.objects.filter(category__pk=pk).order_by('price')

        paginator = Paginator(products_list, 2)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)

        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products_paginator,
            'same_products': same_products,
        }
        return render(request, 'mainapp/products_list.html', content)

    content = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products,
        'hot_product': hot_product,
    }
    return render(request, 'mainapp/products.html', content)


def product(request, pk):
    title = 'Страница товара'

    content = {
        'title': title,
        'links_menu': ProductCategory.objects.all(),
        'product': get_object_or_404(Product, pk=pk),
    }

    return render(request, 'mainapp/product.html', content)


def contacts(request):
    title = 'Контакты'
    locations = []
    file_path = os.path.join(settings.BASE_DIR, 'mainapp/json/contacts.json')
    with open(file_path, 'r', encoding='utf-8') as file_contacts:
        locations = json.load(file_contacts)

    content = {'title': title, 'locations': locations}
    return render(request, 'mainapp/contact.html', content)


def not_found(request, exception):
    return render(request, '404.html', context={'item': 'item'}, status=404)

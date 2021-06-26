from django.shortcuts import render
from itertools import chain

from pprint import pprint

from .models import Product, ProductAttribute, Category
from .fitlers import ProductFilter  


def list_view(request):
    products = Product.objects.all()
    # product_attributes = ProductAttribute.objects.all()

    product_filter = ProductFilter(request.GET, queryset=products)
    products = product_filter.qs
    


    context = {
        'products': products,
        'product_filter': product_filter,

    }
    return render(request, 'product/list_view.html', context)


def product_catalog(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'product/categories_list.html', context)


def cat_filter(request, slug):
    cat = Category.objects.filter(slug=slug).first()
    products = Product.objects.filter(category=cat)  
    product_filter = ProductFilter(request.GET, queryset=products, current_cat=cat)

    products = product_filter.qs

    context = {
        'products': products,
        'product_filter': product_filter,
    }
    return render(request, 'product/list_view.html', context)
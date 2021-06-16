from django.shortcuts import render
from itertools import chain

from .models import Product, ProductAttribute
from .fitlers import ProductFilter  


def list_view(request):
    products = Product.objects.all()
    product_attributes = ProductAttribute.objects.all()

    product_filter = ProductFilter(request.GET, queryset=products)
    products = product_filter.qs




    context = {
        'products': products,
        'product_filter': product_filter,

    }
    return render(request, 'product/list_view.html', context)
from django.shortcuts import render, get_object_or_404, redirect

from product.models import Product
from .forms import ProductForm


def home(request):
    context = {}
    return render(request, 'dashboard/home.html', context)


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST) 
        form.save()   
    else:
        form = ProductForm()

    context = {
        'form': form,
    }
    
    return render(request, 'dashboard/add_product.html', context)

def product_list(request):
    qs = Product.objects.all()
    context = {
        'products': qs,
    }
    return render(request, 'dashboard/product_list.html',context)


def product_edit(request, id):
    instance = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('dashboard:product-list')
    context = {
        'form': form,
    }
    return render(request, 'dashboard/product_edit.html', context)

# def my_view(request, id): 
#     instance = get_object_or_404(MyModel, id=id)
#     form = MyForm(request.POST or None, instance=instance)
#     if form.is_valid():
#         form.save()
#         return redirect('next_view')
#     return render(request, 'my_template.html', {'form': form}) 
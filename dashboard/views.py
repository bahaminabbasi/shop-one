from django.shortcuts import render, get_object_or_404, redirect

from product.models import Category, Product, Brand
from .forms import ProductForm, BrandForm, ProductAttributeForm, ImageForm, FileFieldForm


def home(request):
    context = {}
    return render(request, 'dashboard/home.html', context)


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST) 
        form.save()   
    else:
        form = ProductForm()
    print(ProductForm.__dict__)

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



def one_brand_cat_choose(request):
    categories = Category.objects.all()
    brands = Brand.objects.all()

    if request.method == 'POST':
        category = request.POST['select_categories']
        brand = request.POST['select_brand']
        return redirect('dashboard:two-product', category, brand)
    else:
        brand_form = BrandForm()
    context = {
        'categories': categories,
        'brands': brands,
        'brand_form': brand_form,
    }
    return render(request, 'dashboard/one_brand_cat_choose.html', context)


def two_product(request, category, brand):
    if request.method == 'POST':
        form = ProductForm(request.POST, category=category, brand=brand)  
        if form.is_valid():  
            product = form.save()
            return redirect('dashboard:three-attribute', product)
    else:
        form = ProductForm(category=category, brand=brand)  
    context = {
        'form': form,
    }
    return render(request, 'dashboard/two_product.html', context)


def three_attribute(request, product):
    if request.method == 'POST':
        form = ProductAttributeForm(request.POST, product=product)  
        if form.is_valid():  
            product = form.save()
            return redirect('dashboard:four-images', product)
    else:
        form = ProductAttributeForm(product=product)  
    context = {
        'form': form,
    }
    return render(request, 'dashboard/three_attribute.html', context)


def four_images(request, product):

    if request.method == 'POST':
        form = FileFieldForm(request.POST)
        files = request.FILES
        print()
        print(form.errors)
        print()
        if form.is_valid():
            for f in files:
                print(f)     
        else:
            print()
            print("FAIIIIIIL")
            print()
        return redirect('dashboard:home')
    else:
        form = FileFieldForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboard/four_images.html', context)



def add_brand(request):
    if request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('dashboard:one-brand-cat-choose')
    else:
        return render(request, 'dashboard/one_brand_cat_choose.html')
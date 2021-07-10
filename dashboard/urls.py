from django.urls import path

from .views import (home,
                    add_product,
                    product_list,
                    product_edit,
                    )



app_name = 'dashboard'

urlpatterns = [
    path('', home, name='home'),
    path('add-product/', add_product, name='add-product'),
    path('product_list/', product_list, name='product-list'),
    path('product_edit/<int:id>', product_edit, name='product-edit'),
]


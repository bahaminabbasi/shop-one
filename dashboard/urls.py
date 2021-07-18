from django.urls import path

from .views import (home,
                    add_product,
                    product_list,
                    product_edit,
                    one_brand_cat_choose,
                    two_product,
                    add_brand,
                    three_attribute,
                    four_images,
                    test,
                    )



app_name = 'dashboard'

urlpatterns = [
    path('', home, name='home'),
    path('add_product/', add_product, name='add-product'),
    path('product_list/', product_list, name='product-list'),
    path('product_edit/<int:id>', product_edit, name='product-edit'),
    path('add_brand/', add_brand, name='add-brand'),
    path('test/', test, name='test'),

    # 4 Steps:
    path('one_brand_cat_choose/', one_brand_cat_choose, name='one-brand-cat-choose'),
    path('two_product/<str:category>/<str:brand>/', two_product, name='two-product'),
    path('three_attribute/<str:product>/', three_attribute, name='three-attribute'),
    path('four_images/<str:product>/', four_images, name='four-images'),
]


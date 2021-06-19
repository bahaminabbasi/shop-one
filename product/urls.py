from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import list_view, product_catalog, cat_filter

app_name = 'product'

urlpatterns = [
    path('list-view/', list_view, name="list-view"),
    path('product-catalog/', product_catalog, name="product-catalog"),
    path('cat-filter/<slug:slug>', cat_filter, name='category'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
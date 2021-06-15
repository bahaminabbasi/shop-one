from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import list_view

app_name = 'product'

urlpatterns = [
    path('list-view/', list_view, name="list-view")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
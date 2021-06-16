from django import forms
import django_filters

from .models import *

class ProductFilter(django_filters.FilterSet):
    # price = django_filters.NumberFilter()
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
    # brand = django_filters.ModelMultipleChoiceFilter(
    #                 queryset=Product.objects.values_list('brand', flat=True).distinct(),
    #                 widget=forms.CheckboxSelectMultiple()) 

    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['title', 'slug', 'detail', 'specs', 'status', 'is_featured', 'price']

        # filter_overrides = {
        #     models.CharField: {
        #         'filter_class': django_filters.CharFilter,
        #         'extra': lambda f: {
        #             'lookup_expr': 'icontains',
        #         },
        #     },
        #     models.BooleanField: {
        #         'filter_class': django_filters.BooleanFilter,
        #         'extra': lambda f: {
        #             'widget': forms.CheckboxInput,
        #         },
        #     },
        # }



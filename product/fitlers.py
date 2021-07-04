from django import forms
import django_filters
from django_filters import OrderingFilter

from .models import *


# >>> UserFilter().filters['o'].field.choices
# [
#     ('account', 'User account'),
#     ('-account', 'User account (descending)'),
#     ('first_name', 'First name'),
#     ('-first_name', 'First name (descending)'),
#     ('last_name', 'Last name'),
#     ('-last_name', 'Last name (descending)'),
# ]

class ProductFilter(django_filters.FilterSet):
    def __init__(self, *args, **kwargs):
        self.current_cat = kwargs.pop('current_cat', None)
        self.brands_qs = kwargs.pop('brands_qs', None)
        super(ProductFilter, self).__init__(*args, **kwargs)       
        self.filters['category'] = django_filters.ModelMultipleChoiceFilter(
                field_name='category',
                queryset=Category.objects.filter(parent=self.current_cat.parent, nesting_level=1),
                widget=forms.CheckboxSelectMultiple(),
                )
        self.filters['brand'] = django_filters.ModelMultipleChoiceFilter(
                field_name='brand',
                queryset=self.brands_qs,
                widget=forms.CheckboxSelectMultiple(),
                )
        self.filters['ordering'].field.choices = [('price', 'قیمت'),
                               ('-price', 'قیمت (نزولی)'),]

    ordering = OrderingFilter(
        # tuple-mapping retains order
        fields=(
            ('price', 'price'),
            ),

        # # labels do not need to retain order
        # field_labels={
        #     'price': 'قیمت',
        # }
    )

    # brand = django_filters.ModelMultipleChoiceFilter(
    #     field_name='brand',
    #     queryset=Brand.objects.all(),
    #     widget=forms.CheckboxSelectMultiple(),
    # )

    # class Meta:
    #     model = Product
    #     fields = '__all__'
    #     exclude = ['title', 'slug', 'detail', 'specs', 'status', 'is_featured', 'price']


    


# category = django_filters.ModelMultipleChoiceFilter(
#         field_name='category',
#         queryset=Category.objects.filter(title=self.current_cat),
#         widget=forms.CheckboxSelectMultiple(),
#         )
    # @property
    # def qs(self):
    #     parent = super().qs
    #     cat = getattr(self.request, 'selected_cat', None)
    #     print()
    #     print(cat)
    #     print()



    # price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    # price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')









# class ProductFilter(django_filters.FilterSet):
#     # def __init__(self, *args, **kwargs):
#     #     self.current_cat = kwargs.pop('current_cat', None)
#     #     super(ProductFilter, self).__init__(*args, **kwargs)

#     #     # self.fields['height'].widget = forms.TextInput(attrs={'size':site_id})

#     #     self.category = django_filters.ModelMultipleChoiceFilter(
#     #                                 field_name='category',
#     #                                 queryset=Category.objects.filter(title=self.current_cat),
#     #                                 widget=forms.CheckboxSelectMultiple(),
#     # )

#     category = django_filters.ModelMultipleChoiceFilter(
#         field_name='category',
#         queryset=Category.objects.filter(),
#         widget=forms.CheckboxSelectMultiple(),
#     )

#     brand = django_filters.ModelMultipleChoiceFilter(
#         field_name='brand',
#         queryset=Brand.objects.all(),
#         widget=forms.CheckboxSelectMultiple(),
#     )

#     # price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
#     # price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')



#     # class Meta:
#     #     model = Product
#     #     fields = '__all__'
#     #     exclude = ['title', 'slug', 'detail', 'specs', 'status', 'is_featured', 'price']
    






#     # brand = django_filters.ModelMultipleChoiceFilter(
#     #                 queryset=Product.objects.values_list('brand', flat=True).distinct(),
#     #                 widget=forms.CheckboxSelectMultiple()) 

#     # class Meta:
#     #     model = Product
#     #     fields = '__all__'
#     #     exclude = ['title', 'slug', 'detail', 'specs', 'status', 'is_featured', 'price']

#     #     filter_overrides = {
#     #         models.CharField: {
#     #             'filter_class': django_filters.CharFilter,
#     #             'extra': lambda f: {
#     #                 'lookup_expr': 'icontains',
#     #             },
#     #         },
#     #         models.BooleanField: {
#     #             'filter_class': django_filters.BooleanFilter,
#     #             'extra': lambda f: {
#     #                 'widget': forms.CheckboxInput,
#     #             },
#     #         },
#     #     }



from django.forms import ModelForm, Textarea, widgets, FileField
from product.models import Brand, Product, Category, ProductAttribute, Images
from django import forms




class ProductForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.category = kwargs.pop('category', None)
        self.brand = kwargs.pop('brand', None)
        super().__init__(*args, **kwargs)
        category_obj = Category.objects.filter(title=self.category).first()
        self.fields['category'].initial = category_obj
        brand_obj = Brand.objects.filter(title=self.brand).first()
        self.fields['brand'].initial = brand_obj        

    class Meta:
        model = Product
        exclude = ['slug', 'date', ]
        widgets = {
            'detail': Textarea(attrs={'cols': 1, 'rows': 1}),
            'specs': Textarea(attrs={'cols': 1, 'rows': 1}),
        }



class BrandForm(ModelForm):
    class Meta:
        model = Brand
        exclude = ['detail', ]


class ProductAttributeForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.product = kwargs.pop('product', None)
        super().__init__(*args, **kwargs)
        product_obj = Product.objects.filter(title=self.product).first()
        self.fields['product'].initial = product_obj


    class Meta:
        model = ProductAttribute
        exclude = ['price', ]


class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))


class ImageForm(ModelForm):
    class Meta:
        model = Images
        fields = ['image', 'product']
        # widgets = {
        #     'image': forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True})),
        # }
        field_classes = {'image': forms.FileField}
        widgets = {'image': forms.ClearableFileInput(attrs={'multiple': True})}
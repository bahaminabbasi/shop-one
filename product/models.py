from typing import Tuple
from django.db import models
from django.db.models.fields import DecimalField
from django.utils.html import mark_safe
from django.urls import reverse
from django_filters import parse_version
# from django.http import request




class CustomQuerySet(models.QuerySet):
    def related_categories(self):
        # selected_cat = 'this'
        # cat = Category.objects.filter(title=selected_cat).first()
        # parent_cat = cat.parent
        # if parent_cat is not None:
        #     return Category.objects.filter(parent_cat=parent_cat)
        # return selected_cat
        pass


# Category
class Category(models.Model):
    title               = models.CharField(max_length=100)
    nesting_level       = models.PositiveBigIntegerField(default=1, blank=True, null=True)
    parent              = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    slug                = models.SlugField(max_length=60, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('product:category', kwargs={'slug': self.slug})

    class Meta:
        verbose_name_plural='2. Categories'

    # def image_tag(self):
    #     return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title
    
    objects = CustomQuerySet.as_manager()


# Brand
class Brand(models.Model):
    title=models.CharField(max_length=100)
    # image=models.ImageField(upload_to="brand_imgs/")

    class Meta:
        verbose_name_plural='3. Brands'

    def __str__(self):
        return self.title




# Product Model
class Product(models.Model):
    title=models.CharField(max_length=200)
    slug=models.CharField(max_length=400)
    detail=models.TextField()
    specs=models.TextField()
    price = models.IntegerField(blank=True, null=True, default=17)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    status=models.BooleanField(default=True)
    is_featured=models.BooleanField(default=False)

    class Meta:
        verbose_name_plural='6. Products'

    def __str__(self):
        return self.title

    def get_price(self):
        product = ProductAttribute.objects.filter(product=self).first()
        return product.price



# Color
class Color(models.Model):
    title=models.CharField(max_length=100)
    color_code=models.CharField(max_length=100)

    class Meta:
        verbose_name_plural='4. Colors'

    def color_bg(self):
        return mark_safe('<div style="width:30px; height:30px; background-color:%s"></div>' % (self.color_code))

    def __str__(self):
        return self.title

# Size
class Size(models.Model):
    title=models.CharField(max_length=100)

    class Meta:
        verbose_name_plural='5. Sizes'

    def __str__(self):
        return self.title


# Product Attribute
class ProductAttribute(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    color=models.ForeignKey(Color,on_delete=models.CASCADE)
    size=models.ForeignKey(Size,on_delete=models.CASCADE)
    price=models.PositiveIntegerField(default=0)
    image=models.ImageField(upload_to="product_imgs/",null=True)

    class Meta:
        verbose_name_plural='7. ProductAttributes'

    def __str__(self):
        return self.product.title

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    

# Banner
class Banner(models.Model):
    img=models.ImageField(upload_to="banner_imgs/")
    alt_text=models.CharField(max_length=300)

    class Meta:
        verbose_name_plural='1. Banners'

    def image_tag(self):
        return mark_safe('<img src="%s" width="100" />' % (self.img.url))

    def __str__(self):
        return self.alt_text

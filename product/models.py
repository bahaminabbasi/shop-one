from django.db import models
from django.urls import reverse
from django.utils.html import mark_safe
from A.utils import shamsi_date




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
    

# Brand
class Brand(models.Model):
    title           = models.CharField(max_length=100)
    detail          = models.TextField(default='no details yet')


    # image=models.ImageField(upload_to="brand_imgs/")

    class Meta:
        verbose_name_plural='3. Brands'

    def __str__(self):
        return self.title




# Product Model
class Product(models.Model):
    title               = models.CharField(max_length=200)
    slug                = models.CharField(max_length=400)
    detail              = models.TextField(default='test')
    specs               = models.TextField(default='test')
    price               = models.IntegerField(blank=True, null=True, default=17)
    category            = models.ForeignKey(Category,on_delete=models.CASCADE)
    brand               = models.ForeignKey(Brand,on_delete=models.CASCADE)
    status              = models.BooleanField(default=True)
    is_featured         = models.BooleanField(default=False)
    date                = models.CharField(max_length=200, default=shamsi_date,
                                                blank=True, null=True)

    class Meta:
        verbose_name_plural='6. Products'

    def __str__(self):
        return self.title

    def get_price(self):
        product = ProductAttribute.objects.filter(product=self).first()
        return product.price




# Product Attribute
class ProductAttribute(models.Model):
    product             = models.ForeignKey(Product,on_delete=models.CASCADE)
    color               = models.CharField(max_length=120, blank=True, null=True, default='test')
    description         = models.CharField(max_length=120, blank=True, null=True, default='test')
    price               = models.PositiveIntegerField(default=0)
    more_detail         = models.TextField(default='no details yet')

    class Meta:
        verbose_name_plural='7. ProductAttributes'

    def __str__(self):
        return self.product.title


# Banner
class Banner(models.Model):
    img                 = models.ImageField(upload_to="banner_imgs/")
    alt_text            = models.CharField(max_length=300)

    class Meta:
        verbose_name_plural='1. Banners'

    def image_tag(self):
        return mark_safe('<img src="%s" width="100" />' % (self.img.url))

    def __str__(self):
        return self.alt_text



class Images(models.Model):
    image               = models.ImageField(upload_to="new_pictures/")
    product             = models.ForeignKey(Product, on_delete=models.CASCADE)
    is_main             = models.BooleanField()
    title               = models.CharField(max_length=100, blank=True,
                                             null=True, default=shamsi_date)

    # thumbnail, type = [gallery picture, banner picture, ...]

    class Meta:
        verbose_name_plural='8. Images'

    def __str__(self):
        return self.title


from django.db import models
from django.utils.text import slugify
from sorl.thumbnail import get_thumbnail
from django.utils.html import format_html


# Create your models here.

class Category(models.Model):
    # authentication_classes = [I]
    # permission_classes = [IsSuperUserCanAccess]

    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Product(models.Model):
    category = models.ForeignKey(Category, to_field='id', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="my_picture")
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    # @property
    # def image_preview(self):
    #     if self.image:
    #         _image = get_thumbnail(self.image,
    #                                '300x300',
    #                                upscale=False,
    #                                crop=False,
    #                                quality=100)
    #         return format_html(
    #             '<img src="{}" width="{}" height="{}">'.format(_image.url, _image.width, _image.height))
    #     return ""

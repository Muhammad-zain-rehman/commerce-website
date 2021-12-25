from django.core.validators import FileExtensionValidator
from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    slug = serializers.CharField(read_only=True)

    class Meta:
        model = Category
        fields = ['id, name', 'slug']

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.save()
        return instance

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField(method_name='get_category_name')
    category = serializers.IntegerField()
    title = serializers.CharField()
    author = serializers.CharField()
    description = serializers.CharField()
    image = serializers.ImageField(
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'gif', 'bmp', 'tif', 'tiff', 'eps', 'raw',
                                                               'cr2', 'nef', 'orf', 'sr2', 'png'])])
    slug = serializers.CharField(read_only=True)
    price = serializers.CharField()
    in_stock = serializers.BooleanField(default=True)
    is_active = serializers.BooleanField(default=True)
    created = serializers.DateTimeField()
    updated = serializers.DateTimeField()

    class Meta:
        model = Product
        fields = ['id', 'category', 'title', 'author', 'description', 'slug', 'price', 'in_stock', 'is_active', 'created',
                  'updated']
        extra_kwargs = {
            'price': {'max_digits': 16, 'decimal_places': 2}
        }

    def get_category(self, obj):
        try:
            return obj.category.slug
        except:
            None

    def create(self, validated_data):
        var = validated_data.pop('category')

        category_obj = Category.objects.get(id=var)
        product_obj = Product.objects.create(**validated_data)
        product_obj.category = category_obj
        product_obj.save()
        return product_obj

    # def update(self, instance, validated_data):
    #     var = validated_data.get('category', instance.category)
    #     instance.category = Category.objects.get(id=var)



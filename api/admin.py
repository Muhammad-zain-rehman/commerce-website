from django.contrib import admin
from api.models import Category, Product

# Register your models here.


class CategoryAdmin (admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
    )
    prepopulated_fields = {'slug': ('name',)}

    def get_readonly_fields(self, request, obj=None):
        if obj:
            self.prepopulated_fields = {}
            return self.readonly_fields + ('slug',)
        return self.readonly_fields


admin.site.register(Category, CategoryAdmin),


class ProductAdmin (admin.ModelAdmin):
    list_display = (
        'id', 'category', 'title', 'author', 'description', 'slug', 'price', 'in_stock', 'is_active', 'created',
        'updated'
    )
    prepopulated_fields = {'slug': ('title',)}

    def get_readonly_fields(self, request, obj=None):
        if obj:
            self.prepopulated_fields = {}
            return self.readonly_fields + ('slug',)
        return self.readonly_fields


admin.site.register(Product, ProductAdmin)

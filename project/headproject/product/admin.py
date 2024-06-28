from django.contrib import admin
from product import models
from product.models import Category, Product, Images

class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 2

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','category', ]
    list_filter = ['category']
    #readonly_fields = ('image_tag',)
    inlines = [ProductImageInline]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','parent','status']
    list_filter = ['status']

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Images)

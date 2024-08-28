from import_export.admin import ImportExportModelAdmin
from django.contrib import admin 
from product.resources import CategoryResource,BrandResource,ProductResource
from product.models import Category,Brands,Product


# Register your models here.
class CategoryAdmin(ImportExportModelAdmin):
    resource_class = CategoryResource 
    list_display = ["category_name", "category_code", "description","category_image"]
    
admin.site.register(Category, CategoryAdmin)


class BrandAdmin(ImportExportModelAdmin):
    resource_class = BrandResource 
    list_display = ["brand_name", "brand_code", "description","brand_image"]
    
admin.site.register(Brands, BrandAdmin)


class ProductAdmin(ImportExportModelAdmin):
    resource_class = ProductResource 
    list_display = ["product_name"]
    
admin.site.register(Product, ProductAdmin)





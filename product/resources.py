from import_export import resources
from product.models import Category,Brands,Product



class CategoryResource(resources.ModelResource):

    class Meta:
        model = Category
        
class BrandResource(resources.ModelResource):

    class Meta:
        model = Brands
        
        
        


class ProductResource(resources.ModelResource):

    class Meta:
        model = Product
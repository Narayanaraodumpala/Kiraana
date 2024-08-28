from django.db import models


class Category(models.Model):
    category_name=models.CharField(max_length=50)
    description=models.TextField()
    category_type=models.CharField(max_length=30)
    category_image=models.FileField(upload_to='Categories/',default='none')
    category_code=models.CharField(max_length=50)
    
    def __str__(self):
        return self.category_name +' '+ self.category_code
    
    class Meta:
        db_table='Categories'
        
        
class Brands(models.Model):
    brand_name=models.CharField(max_length=50)
    description=models.TextField()
    
    brand_image=models.FileField(upload_to='Brands/',default='none')
    brand_code=models.CharField(max_length=50)
    
    def __str__(self):
        return self.brand_name +' '+ self.brand_code
    
    class Meta:
        db_table='Brands'
        
class Product(models.Model):
    product_name=models.CharField(max_length=100,unique=True)
    
    
    def __str__(self):
        return self.product_name
    
    class Meta:
        db_table='Product'
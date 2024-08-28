from django.db import models

# Create your models here.


class SuperAdmin(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
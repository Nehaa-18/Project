from django.contrib.auth.models import AbstractUser
from django.db import models
# from .models import Category, Subcategory

# Create your models here.


class CustomUser(AbstractUser):
    usertype = models.CharField(max_length=20)  # Add any additional fields you need


    
    def __str__(self):
       return self.email


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    price_per_day = models.DecimalField(max_digits=10, decimal_places=1)
    category = models.CharField(max_length=50, default='Uncategorized')
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    # subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name='products')
    availability = models.BooleanField(default=True)
    #quantity = models.PositiveIntegerField(default=1) 
    image = models.ImageField(upload_to='product_images/', default='default-image.jpg')

    def __str__(self):
        return self.name
    


# class Category(models.Model):
#     name = models.CharField(max_length=50, unique=True)

#     def __str__(self):
#         return self.name
    

# class Subcategory(models.Model):
#     name = models.CharField(max_length=50)
#     category = models.ForeignKey('Category', on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name



class Wishlist(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f'Wishlist for {self.user}'

class Warehouse(models.Model):
    warehouse_id = models.AutoField(primary_key=True)
    warehouse_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=128)  # You should use a secure way to store passwords in a real application

    def __str__(self):
        return self.warehouse_name
    


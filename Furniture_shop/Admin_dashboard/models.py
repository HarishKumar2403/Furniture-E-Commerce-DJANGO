from django.db import models


class Admin_Member(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=10)
    email=models.CharField(max_length=50)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    confirm_password=models.CharField(max_length=20,null=True,blank=True)

    def __str__(self):
        return self.firstname 
    
class Product(models.Model):
    
    #Product Details
    
    Category_name = models.CharField(max_length=50, choices=(
        ('Bed', 'Bed'),
        ('Gaming-Chair', 'Gaming-Chair'),
        ('Tv-Units','Tv-Units'),
        ('Sofa','Sofa'),
        ('Wardrobes','Wardrobes')
    ))
    product_name=models.TextField()
    product_price=models.BigIntegerField(default=1)
    product_size = models.CharField(max_length=100,null=True,blank=True)
    quantity=models.IntegerField()
    new=models.BooleanField(default=False,help_text="0-default,1-Trending")
    trending=models.BooleanField(default=False,help_text="0-default,1-Trending")
    out_of_stock=models.BooleanField(default=False,help_text="0-default,1-Trending")
    product_image1=models.ImageField(upload_to='product')
    product_image2=models.ImageField(upload_to='product')
    product_image3=models.ImageField(upload_to='product')
    product_image4=models.ImageField(upload_to='product')
    product_image5=models.ImageField(upload_to='product')

    #Product Description:
    product_description=models.TextField()

    #Warranty
    warranty=models.TextField()

    def __str__(self):
        return self.product_name
    

    

    

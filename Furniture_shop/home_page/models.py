from django.db import models
from Admin_dashboard.models import *


class Member(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    gender = models.CharField(max_length=6, choices=[('Male', 'Male'), ('Female', 'Female')])
    mobile_number = models.CharField(max_length=10)
    email=models.CharField(max_length=50,unique=True)
    username=models.CharField(max_length=20,unique=True)
    password=models.CharField(max_length=20)

    def __str__(self):
        return self.firstname 
      

class Cart(models.Model):
    Product=models.ForeignKey(Product, on_delete=models.CASCADE,null=True,blank=True)
    user = models.ForeignKey(Member, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    cart_price = models.DecimalField(max_digits=10, decimal_places=2, default=0,null=True,blank=True)
    status=models.CharField(max_length=50,default='Pending')

class Order(models.Model):
    Product=models.ForeignKey(Product, on_delete=models.CASCADE,null=True,blank=True)
    user = models.ForeignKey(Member, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    cart_price = models.DecimalField(max_digits=10, decimal_places=2, default=0,null=True,blank=True)
    status=models.CharField(max_length=50,default='Pending')
    

class Checkout(models.Model):
    carts = models.ManyToManyField(Order, related_name='checkouts')
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    phone = models.IntegerField()
    email = models.EmailField()
    payment = models.CharField(max_length=50)
    

    def __str__(self):
        return f"Checkout by {self.firstname} {self.lastname}"
    

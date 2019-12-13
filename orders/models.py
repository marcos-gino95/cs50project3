from django.db import models
from django.conf import settings

# Create your models here.
class Regular_Pizza(models.Model):
    type = models.CharField(max_length = 40)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    items = models.IntegerField(default = 0)
    size = models.CharField(max_length = 10)
    def __str__(self):
        return f"{self.type}, {self.size} -> {self.price}"

class Sicilian_Pizza(models.Model):
    type = models.CharField(max_length = 40)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    items = models.IntegerField(default = 0)
    size = models.CharField(max_length = 10)
    def __str__(self):
        return f"{self.type}, {self.size} -> {self.price}"

class Toppings(models.Model):
    type = models.CharField(max_length = 40)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    def __str__(self):
        return f"{self.type}"

class Subs(models.Model):
    type = models.CharField(max_length = 40)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    size = models.CharField(max_length = 10)
    def __str__(self):
        return f"{self.type}, {self.size} -> {self.price}"

class Pasta(models.Model):
    type = models.CharField(max_length = 40)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    def __str__(self):
        return f"{self.type}"

class Salad(models.Model):
    type = models.CharField(max_length = 40)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    def __str__(self):
        return f"{self.type}"

class Dinner_Platters(models.Model):
    type = models.CharField(max_length = 40)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    size = models.CharField(max_length = 40)
    def __str__(self):
        return f"{self.type}, {self.size} -> {self.price}"

class Order_Number(models.Model):
    order_num = models.IntegerField()
    username = models.CharField(max_length=20)
    status = models.CharField(max_length=10)
    def __str__(self):
        return f"Order nro: {self.id}"

class Order(models.Model):
    number = models.IntegerField()
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    def __str__(self):
        return f"{self.number} -> {self.description}, {self.price}"



##class Orders(models.Model):
##    order_number = models.IntegerField()
##    price = models.DecimalField(max_digits=4, decimal_places=2)
##    item = models.CharField(max_length = 40)
##    def __str__(self):
##        return f"{self.order_number}: {self. item} {self.price}"

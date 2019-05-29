from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class NotPizza(models.Model):
    name = models.CharField(max_length=64)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=None, null=True, related_name="dishes")
    regprice = models.DecimalField(decimal_places=2, max_digits=4, default=0)
    large = models.BooleanField(default=False)
    largeprice = models.DecimalField(decimal_places=2, max_digits=4, null=True, blank=True)
    extratoppings= models.BooleanField(default=False)


    def __str__(self):
        return f"{self.name} costs {self.regprice} is of category {self.category}"

class NotPizzaToppings(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(decimal_places=2, max_digits=4, default=0)
    sub = models.ManyToManyField(NotPizza, blank=True, related_name="toppings")

    def __str__(self):
        return f"{self.name}"

class Pizza(models.Model):
    name = models.CharField(max_length=64)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=None, null=True, related_name="pizza")
    regprice = models.DecimalField(decimal_places=2, max_digits=4, default=0)
    large = models.BooleanField(default=False)
    largeprice = models.DecimalField(decimal_places=2, max_digits=4, null=True, blank=True)
    topamount = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return f"{self.name} costs {self.regprice} is of category {self.category}"

class PizzaToppings(models.Model):
    name = models.CharField(max_length=64)
    sub = models.ManyToManyField(Pizza, blank=True, related_name="piztop")

    def __str__(self):
        return f"{self.name}"

class CartItems(models.Model):
    user = models.CharField(max_length=64)
    size = models.CharField(max_length=5, null=True)
    item = models.CharField(max_length=64)
    price = models.DecimalField(decimal_places=2, max_digits=4, default=0)
    topping = models.CharField(max_length=64,null=True, blank=True)

    def __str__(self):
        return f"{self.user} added {self.item} to their shoppingcart with size {self.size} and price {self.price}"

class ViewOrders(models.Model):
    user = models.CharField(max_length=64)
    size = models.CharField(max_length=5, null=True)
    item = models.CharField(max_length=64)
    topping = models.CharField(max_length=64,null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=4, default=0)

    def __str__(self):
        return f"{self.user} orders {self.item}"

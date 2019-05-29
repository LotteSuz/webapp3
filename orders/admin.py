from django.contrib import admin
from .models import NotPizza, NotPizzaToppings, Category, Pizza, PizzaToppings, CartItems, ViewOrders

# Register your models here.
admin.site.register(NotPizza)
admin.site.register(NotPizzaToppings)
admin.site.register(Category)
admin.site.register(Pizza)
admin.site.register(PizzaToppings)
admin.site.register(CartItems)
admin.site.register(ViewOrders)

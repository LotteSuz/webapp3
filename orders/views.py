from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Category, NotPizza, NotPizzaToppings, Pizza, PizzaToppings, CartItems, ViewOrders
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
def index(request):
    context = {
        "pastas": NotPizza.objects.filter(category__name="Pasta"),
        "salads": NotPizza.objects.filter(category__name="Salads"),
        "subs": NotPizza.objects.filter(category__name="Subs"),
        "plates": NotPizza.objects.filter(category__name="Plates"),
        "sicilians": Pizza.objects.filter(category__name="Sicilian"),
        "regulars": Pizza.objects.filter(category__name="Regular")
    }
    return render(request, "orders/index.html", context)

def register(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        if not request.POST["first_name"] or not request.POST["last_name"] or not request.POST["username"]:
            return render(request, "register.html", {"message":"You must provide a full name and username."})
        elif not request.POST["email"]:
            return render(request, "register.html", {"message":"You must provide an emailadress."})
        elif not request.POST["password"] or not request.POST["password2"]:
            return render(request, "register.html", {"message":"You must provide a password."})
        elif not password == password2:
            return render(request, "register.html", {"message":"Your password and confirmation should be the same."})

        if User.objects.filter(email=email).exists():
             return render(request, "register.html", {"message":"An account with this emailadress already exists, please log in."})

        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return render(request, "orders/login.html", {"message":"Registered. You can log in now."})
    else:
        return render(request, "orders/register.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "orders/login.html", {"message": "Invalid credentials."})
    else:
        return render(request, "orders/login.html")


def logout_view(request):
    logout(request)
    return render(request, "orders/login.html", {"message": "Logged out."})

def dish(request, name):
    try:
        item = NotPizza.objects.get(name=name)
    except:
        try:
            item = Pizza.objects.get(name=name)
        except:
            item = "Nothing"
    type = str(item.category)
    if (type == "Sicilian" or type == "Regular"):
        toppings = PizzaToppings.objects.all()
        number = int(item.topamount)
        pizza = True
        sub = False
    elif (type == "Subs"):
        sub = True
        pizza = False
        extras = item.extratoppings
        if extras:
            number = 4
            toppings = NotPizzaToppings.objects.all()
        else:
            number = 1
            toppings = NotPizzaToppings.objects.get(name="Cheese")
            print(toppings)
    else:
        sub = False
        toppings = None
        number = 0
        pizza = False
    context = {
        "item": item,
        "toppings": toppings,
        "number": number,
        "pizza": pizza,
        "sub": sub
    }
    return render(request, "orders/dish.html", context)

def cart(request):
    if request.method == "POST":
        meal = request.POST["dishname"]
        try:
            item = NotPizza.objects.get(name=meal)
        except:
            item = Pizza.objects.get(name=meal)
        curruser = request.user
        size = request.POST["size"]
        if size == "Small":
            money = item.regprice
        else:
            money = item.largeprice

        type = str(item.category)
        if (type == "Sicilian" or type == "Regular"):
            if (item.topamount == 1):
                topping = request.POST["1"]
            elif (item.topamount == 2):
                topping = request.POST["1"] + " & " + request.POST["2"]
            elif (item.topamount == 3):
                topping = request.POST["1"] + " & " + request.POST["2"] + " & " + request.POST["3"]
            else:
                topping = None
        else:
            topping = None
        print(topping)

        new = CartItems(user=curruser, size=size, item=meal, price=money, topping=topping)
        new.save()
        total = 0
        amount = 0
        cartitems = CartItems.objects.filter(user=curruser)
        for item in cartitems:
            amount += 1
            total += item.price
        context = {
            "cartitems": cartitems,
            "user": curruser,
            "total": total,
            "amount": amount,
            "topping": topping
        }
        return render(request, "orders/cart.html", context)
    else:
        curruser = request.user
        total = 0
        amount = 0
        cartitems = CartItems.objects.filter(user=curruser)
        for item in cartitems:
            amount += 1
            total += item.price
        context = {
            "cartitems": cartitems,
            "user": curruser,
            "total": total,
            "amount": amount
        }
        return render(request, "orders/cart.html", context)

def order(request):
    curruser = request.user
    orderitems = CartItems.objects.filter(user=curruser)
    print(orderitems)
    for item in orderitems:
        print(item)
        print(item.price)
        topping = item.topping
        tryout = item.price
        user = item.user
        size = item.size
        item = item.item
        new = ViewOrders(user=user, size=size, item=item, price=tryout, topping=topping)
        new.save()
    CartItems.objects.filter(user=curruser).delete()
    return redirect("index")

@user_passes_test(lambda u: u.is_superuser)
def deliveries(request):
    context = {
        "orders": ViewOrders.objects.all()
    }
    return render(request, "orders/deliveries.html", context)

def ordercomplete(request, user):
    ViewOrders.objects.filter(user=user).delete()
    return redirect("deliveries")

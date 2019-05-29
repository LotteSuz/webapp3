from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login_view"),
    path("logout_view/", views.logout_view, name="logout_view"),
    path("dish/<str:name>/", views.dish, name="dish"),
    path("cart/", views.cart, name="cart"),
    path("deliveries/", views.deliveries, name="deliveries"),
    path("order/", views.order, name="order"),
    path("ordercomplete/<str:user>", views.ordercomplete, name="ordercomplete")
]

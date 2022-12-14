from django.shortcuts import render
from rest_framework.generics import ListAPIView
from cart.models import Cart, Adresses, Checkout
from cart.serializers import CartListSerializer, AdressesListSerializer, CheckoutListSerializer
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from menu.models import Food
from cart.cart import Cart_pay
from cart.forms import CartAddProductForm


class CartList(ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartListSerializer
    lookup_field = 'id'


class AdressesList(ListAPIView):
    queryset = Adresses.objects.all()
    serializer_class = AdressesListSerializer
    lookup_field = 'id'


class CheckoutList(ListAPIView):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutListSerializer
    lookup_field = 'id'


@require_POST
def cart_add(request, food_id):
    cart = Cart_pay(request)
    food = get_object_or_404(Food, id=food_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(food=food,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, food_id):
    cart = Cart_pay(request)
    food = get_object_or_404(Food, id=food_id)
    cart.remove(food)
    return redirect('cart:cart_detail')



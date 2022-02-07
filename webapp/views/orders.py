from django.shortcuts import render, redirect
from django.views import View

from webapp.forms import ClientForm
from webapp.models import Client, Cart, Order


class OrderView(View):
    def post(self, request, *args, **kwargs):
        form = ClientForm(data=request.POST)
        new_client = None
        if form.is_valid():
            name = form.cleaned_data.get('name')
            address = form.cleaned_data.get('address')
            telephone = form.cleaned_data.get('telephone')
            new_client = Client.objects.create(name=name,
                                               address=address,
                                               telephone=telephone)
        carts = Cart.objects.all()
        for cart in carts:
            order = Order()
            order.client = new_client
            order.product = cart.product
            order.number = cart.number
            order.save()
            cart.product.balance = cart.product.balance - cart.number
            cart.product.save()
            cart.delete()
        return render(request, 'order/index.html')

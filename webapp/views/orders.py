from django.shortcuts import render, redirect
from django.views import View

from webapp.models import Client, Cart, Order, Product


class OrderView(View):
    def post(self, request, *args, **kwargs):
        products = request.session.get('products', {})
        print(products)
        product_ids = products.keys()
        new_products = Product.objects.filter(id__in=product_ids)
        for product in new_products:
            order = Order()
            if request.user.is_authenticated:
                order.client = request.user
            else:
                order.client = None
            order.product = product
            for k, v in products.items():
                if k == str(product.id):
                    order.number = v
                    product.balance = product.balance - v
                    product.save()
            order.save()

        products = {}
        request.session['products'] = products

        # carts = Cart.objects.all()
        # for cart in carts:
        #     order = Order()
        #     order.client = new_client
        #     order.product = cart.product
        #     order.number = cart.number
        #     order.save()
        #     cart.product.balance = cart.product.balance - cart.number
        #     cart.product.save()
        #     cart.delete()
        return render(request, 'order/index.html')

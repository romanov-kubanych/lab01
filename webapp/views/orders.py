from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView

from webapp.models import Order, Product


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
        return render(request, 'order/index.html')


class MyOrderView(ListView):
    model = Order
    template_name = 'orders.html'
    permission_required = 'auth.view_user'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        objects = Order.objects.filter(client_id=self.request.user.id)
        context["objects"] = objects
        return context


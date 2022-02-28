from django.shortcuts import redirect, get_object_or_404, render
from django.views import View

from webapp.models import Product


class CartAddView(View):
    def post(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=kwargs['pk'])
        if product.balance > 0:
            products = request.session.get('products', {})
            if products:
                if str(product.id) not in products.keys():
                    products[product.id] = 1
                else:
                    for item, value in products.items():
                        if value < product.balance:
                            if int(item) == product.id:
                                new_value = value+1
                                products[item] = new_value
            else:
                products[product.id] = 1
            request.session['products'] = products
        return redirect('product_index')


class CartIndexView(View):
    def get(self, request, *args, **kwargs):
        records = {}
        quantity = {}
        sum = {}
        total = 0
        products = request.session.get('products', {})
        product_ids = products.keys()
        new_products = Product.objects.filter(id__in=product_ids)
        for product in new_products:
            records[product.id] = product
            quantity[product.id] = products[str(product.id)]

        for key, value in records.items():
            for k, v in quantity.items():
                if value.id == k:
                    sum[value.id] = value.price*v
        for key, value in sum.items():
            total += value
        context = {
            'quantity': quantity,
            'records': records,
            'sum': sum,
            'total': total,
        }
        return render(request, 'carts/index.html', context)


class CartDeleteView(View):
    def post(self, request, *args, **kwargs):
        product_id = kwargs['pk']
        products = request.session.get('products', {})
        if products:
            products.pop(str(product_id))
        request.session['products'] = products
        return redirect('cart_view')

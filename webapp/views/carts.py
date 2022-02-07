from django.shortcuts import redirect, get_object_or_404, render
from django.views import View

from forms import ClientForm
from webapp.models import Product, Cart


class CartAddView(View):
    def post(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=kwargs['pk'])
        if product.balance > 0:
            current_record = product.cart.filter(product=product.pk)
            if current_record:
                cart = get_object_or_404(Cart, product=product)
                print(cart)
                if cart.number <= product.balance:
                    number = cart.number
                    number += 1
                    cart.number = number
                    cart.save()
            else:
                new_record = Cart.objects.create(product=product, number=1)
        return redirect('product_index')


class CartIndexView(View):
    def get(self, request, *args, **kwargs):
        carts = Cart.objects.all()
        form = ClientForm
        records = []
        sum = 0
        for cart in carts:
            sum = sum + cart.number*cart.product.price
        context = {
            'records': records,
            'carts': carts,
            'sum': sum,
            'form': form
        }
        return render(request, 'carts/index.html', context)


class CartDeleteView(View):
    def post(self, request, *args, **kwargs):
        cart = get_object_or_404(Cart, pk=kwargs['pk'])
        cart.delete()
        return redirect('cart_view')

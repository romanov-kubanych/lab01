from django.shortcuts import render

from webapp.models import Product


def index_view(request):
    products = Product.objects.order_by('category')
    return render(request, 'index_view.html', {'products': products})

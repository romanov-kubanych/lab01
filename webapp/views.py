from django.shortcuts import render, redirect, get_object_or_404

from webapp.models import Product


def index_view(request):
    products = Product.objects.order_by('category')
    return render(request, 'index_view.html', {'products': products})


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)

    return render(request, 'product_view.html', {'product': product})
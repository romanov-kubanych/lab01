from django.shortcuts import render, redirect, get_object_or_404

from webapp.forms import ProductForm
from webapp.models import Product


def index_view(request):
    products = Product.objects.all().order_by('category', 'title').filter(balance__gt=0)
    return render(request, 'index_view.html', {'products': products})


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_view.html', {'product': product})


def create_view(request):
    if request.method == 'GET':
        form = ProductForm()
        return render(request, 'product_create.html', {"form": form})
    else:
        form = ProductForm(data=request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')
            category = form.cleaned_data.get('category')
            balance = form.cleaned_data.get('balance')
            price = form.cleaned_data.get('price')
            new_task = Product.objects.create(title=title,
                                              description=description,
                                              category=category,
                                              balance=balance,
                                              price=price)
            return redirect('product_view', pk=new_task.pk)
        return render(request, 'product_create.html', {"form": form})

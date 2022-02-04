from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import DeleteView, DetailView

from webapp.forms import ProductForm
from webapp.models import Product


def index_view(request):
    products = Product.objects.all().order_by('category', 'title').filter(balance__gt=0)
    return render(request, 'products/index.html', {'products': products})


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/view.html'
# def product_view(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     return render(request, 'products/view.html', {'product': product})


def create_view(request):
    if request.method == 'GET':
        form = ProductForm()
        return render(request, 'products/create.html', {"form": form})
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
        return render(request, 'products/create.html', {"form": form})


def update_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        form = ProductForm(initial={
            'title': product.title,
            'description': product.description,
            'category': product.category,
            'balance': product.balance,
            'price': product.price
        })
        return render(request, 'products/update.html', {'form': form, 'product': product})
    else:
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product.title = form.cleaned_data.get('title')
            product.description = form.cleaned_data.get('description')
            product.category = form.cleaned_data.get('category')
            product.balance = form.cleaned_data.get('balance')
            product.price = form.cleaned_data.get('price')
            product.save()
            return redirect('product_view', pk=product.pk)
        return render(request, 'products/update.html', {'form': form, 'product': product})


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/delete.html'

    def get_success_url(self):
        return reverse('product_index')

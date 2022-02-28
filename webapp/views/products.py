from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import DeleteView, DetailView, ListView, CreateView, UpdateView

from webapp.forms import ProductForm, SearchForm
from webapp.models import Product


class ProductIndexView(ListView):
    model = Product
    template_name = 'products/index.html'
    context_object_name = 'products'
    paginate_by = 5
    paginate_orphans = 0

    def get(self, request, *args, **kwargs):
        self.form = self.get_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(title__icontains=self.search_value) | Q(category__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset.filter(balance__gt=0).order_by('category', 'title')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = SearchForm()
        if self.search_value:
            context['form'] = SearchForm(initial={"search": self.search_value})
            context['search'] = self.search_value
        return context

    def get_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data.get('search')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/view.html'


class ProductCreateView(PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "products/create.html"
    permission_required = 'webapp.add_product'

    def get_success_url(self):
        return reverse('product_view', kwargs={'pk': self.object.pk})


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "products/update.html"
    permission_required = 'webapp.change_product'

    def get_success_url(self):
        return reverse('product_view', kwargs={'pk': self.object.pk})


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'products/delete.html'
    permission_required = 'webapp.delete_product'

    def get_success_url(self):
        return reverse('product_index')

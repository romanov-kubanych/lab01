from django import forms
from django.forms import widgets

from webapp.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = []


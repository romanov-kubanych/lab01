from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets

from webapp.models import Product, Client


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = []

    def clean_balance(self):
        balance = self.cleaned_data['balance']
        if balance <= 0:
            raise ValidationError(
                f"Значение баланса должно быть больше нуля, '{balance}' не подходит")
        return balance


class SearchForm(forms.Form):
    search = forms.CharField(max_length=30, required=False, label="Найти")


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        exclude = []


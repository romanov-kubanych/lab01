from django import forms
from django.forms import widgets

from webapp.models import STATUS_CHOICES


class ProductForm(forms.Form):
    title = forms.CharField(max_length=100,
                            required=True,
                            label="Наименование",
                            error_messages={"required": "Поле обязательно для заполнения",
                                            "max_length": "Максимальная длина поля 100"})
    category = forms.ChoiceField(required=True,
                                 label="Статус",
                                 choices=STATUS_CHOICES,
                                 initial=STATUS_CHOICES[0][1],
                                 error_messages={"required": "Поле обязательно для заполнения",
                                                 "max_length": "Максимальная длина поля 100"}
                                 )
    description = forms.CharField(max_length=2000, required=True, label="Описание",
                                  widget=widgets.Textarea(attrs={"rows": 5, "cols": 50}),
                                  error_messages={"required": "Поле обязательно для заполнения",
                                                  "max_length": "Максимальная длина поля 2000"})
    balance = forms.IntegerField(min_value=0, required=True, label='Остаток',
                                 error_messages={"required": "Поле обязательно для заполнения"})
    price = forms.DecimalField(max_digits=7, decimal_places=2, label='Цена')

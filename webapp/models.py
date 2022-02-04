from django.db import models

STATUS_CHOICES = [('other', 'Разное'), ('smartphone', 'Смартфон'), ('notebook', 'Ноутбук'), ('tv', 'Телевизор')]


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')
    category = models.CharField(max_length=100, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0], verbose_name='Категория')
    balance = models.IntegerField(verbose_name='Остаток')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Цена")

    def __str__(self):
        return f'{self.pk}. {self.title}: {self.description}'

    class Meta:
        db_table = 'Products'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

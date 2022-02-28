from django.db import models

STATUS_CHOICES = [('other', 'Разное'), ('smartphone', 'Смартфон'), ('notebook', 'Ноутбук'), ('tv', 'Телевизор')]


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')
    category = models.CharField(max_length=100,
                                choices=STATUS_CHOICES,
                                default=STATUS_CHOICES[0][0],
                                verbose_name='Категория')
    balance = models.IntegerField(verbose_name='Остаток')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Цена")

    def __str__(self):
        return f'{self.pk}. {self.title}: {self.description}'

    class Meta:
        db_table = 'Products'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Cart(models.Model):
    product = models.ForeignKey('webapp.Product',
                                on_delete=models.CASCADE,
                                verbose_name='Товар',
                                related_name='cart')
    number = models.IntegerField(verbose_name='Количество')

    class Meta:
        db_table = 'Cart'
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def get_sum(self):
        return self.product.price * self.number


class Client(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    address = models.CharField(max_length=100, verbose_name='Адрес')
    telephone = models.CharField(max_length=20, verbose_name='Телефон')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    def __str__(self):
        return f'{self.pk}. {self.name}: {self.address}'

    class Meta:
        db_table = 'Clients'
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Order(models.Model):
    client = models.ForeignKey('webapp.Client',
                               on_delete=models.CASCADE,
                               verbose_name='Клиент',
                               related_name='order')
    product = models.ForeignKey('webapp.Product',
                                on_delete=models.CASCADE,
                                verbose_name='Товар',
                                related_name='order')
    number = models.IntegerField(verbose_name='Количество товара')

    class Meta:
        db_table = 'Orders'
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
# Generated by Django 4.0.1 on 2022-01-07 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Наименование')),
                ('description', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Описание')),
                ('category', models.CharField(choices=[('other', 'Разное'), ('smartphone', 'Смартфон'), ('notebook', 'Ноутбук'), ('tv', 'Телевизор')], default='other', max_length=100, verbose_name='Категория')),
                ('balance', models.IntegerField(verbose_name='Остаток')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'db_table': 'Products',
            },
        ),
    ]

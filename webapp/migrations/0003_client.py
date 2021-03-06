# Generated by Django 4.0.1 on 2022-02-07 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес')),
                ('telephone', models.CharField(max_length=20, verbose_name='Телефон')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
                'db_table': 'Clients',
            },
        ),
    ]

# Generated by Django 3.2 on 2024-03-29 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0009_remove_checkout_product_checkout_carts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='cart_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
    ]
# Generated by Django 4.0.3 on 2024-03-08 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_dashboard', '0004_alter_product_product_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Category_name',
            field=models.CharField(choices=[('Bed', 'Bed'), ('Gaming-Chair', 'Gaming-Chair'), ('Tv-Units', 'Tv-Units'), ('Sofa', 'Sofa'), ('Wardrobes', 'Wardrobes')], max_length=50),
        ),
    ]

# Generated by Django 5.0.3 on 2024-03-22 05:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0003_checkout'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home_page.member'),
        ),
    ]

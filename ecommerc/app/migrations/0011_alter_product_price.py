# Generated by Django 4.0.5 on 2022-07-13 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_order_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]

# Generated by Django 4.0.5 on 2022-07-07 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='orderstatus',
            field=models.CharField(choices=[('pending', 'pending'), ('accepted', 'accepted'), ('on the way', 'on the way'), ('delivery', 'delivery')], default='panding', max_length=100),
        ),
    ]

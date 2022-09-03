# Generated by Django 4.0.5 on 2022-07-07 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('image', models.FileField(max_length=200, upload_to='')),
                ('price', models.IntegerField()),
                ('descriptions', models.CharField(max_length=200)),
                ('unit', models.CharField(choices=[('kg', 'Kg'), ('darjan', 'Darjan')], default='Kg', max_length=100)),
                ('totalquantites', models.PositiveIntegerField()),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('order_date', models.DateTimeField()),
                ('quantites', models.PositiveIntegerField(default='1')),
                ('unit', models.CharField(choices=[('kg', 'Kg'), ('darjan', 'Darjan')], default='Kg', max_length=50)),
                ('descriptions', models.CharField(max_length=100)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='app.product')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]

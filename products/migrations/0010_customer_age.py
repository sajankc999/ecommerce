# Generated by Django 4.2.8 on 2024-01-22 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_cart_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='age',
            field=models.IntegerField(default=18),
        ),
    ]
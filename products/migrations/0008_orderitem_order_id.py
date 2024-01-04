# Generated by Django 4.2.8 on 2024-01-04 04:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_order_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='order_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.order'),
            preserve_default=False,
        ),
    ]
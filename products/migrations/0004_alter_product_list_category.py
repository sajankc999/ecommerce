# Generated by Django 4.2.8 on 2024-01-02 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_cart_customer_alter_customer_user_review_orderitem_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_list',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category'),
        ),
    ]
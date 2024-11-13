# Generated by Django 5.0.6 on 2024-11-13 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0001_initial'),
        ('Checkout', '0010_alter_checkout_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='cart',
            field=models.ManyToManyField(null=True, related_name='orders', to='Cart.cart'),
        ),
    ]
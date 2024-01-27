# Generated by Django 5.0.1 on 2024-01-27 12:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0013_remove_cart_items"),
    ]

    operations = [
        migrations.AddField(
            model_name="cart",
            name="items",
            field=models.ManyToManyField(through="store.CartItem", to="store.product"),
        ),
    ]

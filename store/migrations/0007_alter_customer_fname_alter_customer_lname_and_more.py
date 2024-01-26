# Generated by Django 5.0.1 on 2024-01-26 16:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0006_rename_first_name_customer_fname_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="fname",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="customer",
            name="lname",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="customer",
            name="phone",
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name="customer",
            name="username",
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
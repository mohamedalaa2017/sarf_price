# Generated by Django 4.2.7 on 2023-12-04 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "exchange_rates",
            "0002_alter_currency_options_alter_currency_prices_options_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="currency",
            name="country",
            field=models.CharField(max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name="currency",
            name="name",
            field=models.CharField(max_length=64, unique=True),
        ),
    ]

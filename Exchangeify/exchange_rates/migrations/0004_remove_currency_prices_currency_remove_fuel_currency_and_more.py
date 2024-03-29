# Generated by Django 4.2.7 on 2023-12-07 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("exchange_rates", "0003_alter_currency_country_alter_currency_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="currency_prices",
            name="currency",
        ),
        migrations.RemoveField(
            model_name="fuel",
            name="currency",
        ),
        migrations.RemoveField(
            model_name="fuel",
            name="fuel",
        ),
        migrations.DeleteModel(
            name="Fuel_Types",
        ),
        migrations.RemoveField(
            model_name="gold",
            name="currency",
        ),
        migrations.RemoveField(
            model_name="gold",
            name="karat",
        ),
        migrations.DeleteModel(
            name="Currency",
        ),
        migrations.DeleteModel(
            name="Currency_Prices",
        ),
        migrations.DeleteModel(
            name="Fuel",
        ),
        migrations.DeleteModel(
            name="Gold",
        ),
        migrations.DeleteModel(
            name="Karat",
        ),
    ]

# Generated by Django 4.2.7 on 2023-12-04 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("exchange_rates", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="currency",
            options={"verbose_name": "Currency", "verbose_name_plural": "Currencies"},
        ),
        migrations.AlterModelOptions(
            name="currency_prices",
            options={
                "verbose_name": "Currency_Prices",
                "verbose_name_plural": "Currencies_Prices",
            },
        ),
        migrations.AlterModelOptions(
            name="fuel",
            options={"verbose_name": "Fuel", "verbose_name_plural": "Fuel"},
        ),
        migrations.AlterModelOptions(
            name="fuel_types",
            options={"verbose_name": "Fuel_Types", "verbose_name_plural": "Fuel_Types"},
        ),
        migrations.AlterModelOptions(
            name="gold",
            options={"verbose_name": "Gold", "verbose_name_plural": "Gold"},
        ),
        migrations.AlterModelOptions(
            name="karat",
            options={"verbose_name": "Karat", "verbose_name_plural": "Karat"},
        ),
        migrations.AlterField(
            model_name="currency",
            name="abbreviation",
            field=models.CharField(max_length=3, unique=True),
        ),
    ]

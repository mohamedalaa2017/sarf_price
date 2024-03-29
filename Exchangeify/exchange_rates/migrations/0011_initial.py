# Generated by Django 4.2.7 on 2023-12-07 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("exchange_rates", "0010_remove_currency_prices_currency_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Currency",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("country", models.CharField(max_length=64, unique=True)),
                ("name", models.CharField(max_length=64, unique=True)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="20%y/%m/%d"),
                ),
                ("abbreviation", models.CharField(max_length=3, unique=True)),
            ],
            options={
                "verbose_name": "Currency",
                "verbose_name_plural": "Currency",
            },
        ),
        migrations.CreateModel(
            name="Fuel_Types",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=64)),
            ],
            options={
                "verbose_name": "Fuel_Types",
                "verbose_name_plural": "Fuel_Types",
            },
        ),
        migrations.CreateModel(
            name="Gold_Types",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=64)),
            ],
            options={
                "verbose_name": "Karat",
                "verbose_name_plural": "Karat",
            },
        ),
        migrations.CreateModel(
            name="Gold",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("buy_price", models.FloatField(blank=True, null=True)),
                ("sell_price", models.FloatField(blank=True, null=True)),
                ("prev_close", models.CharField(blank=True, max_length=64, null=True)),
                ("day_range", models.CharField(blank=True, max_length=64, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "currency",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="gold_currency",
                        to="exchange_rates.currency",
                    ),
                ),
                (
                    "karat",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="gold",
                        to="exchange_rates.gold_types",
                    ),
                ),
            ],
            options={
                "verbose_name": "Gold",
                "verbose_name_plural": "Gold",
            },
        ),
        migrations.CreateModel(
            name="Fuel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("buy_price", models.FloatField(blank=True, null=True)),
                ("sell_price", models.FloatField(blank=True, null=True)),
                ("change", models.CharField(blank=True, max_length=64, null=True)),
                ("prev_close", models.CharField(blank=True, max_length=64, null=True)),
                ("day_range", models.CharField(blank=True, max_length=64, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "currency",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="fuel_currency",
                        to="exchange_rates.currency",
                    ),
                ),
                (
                    "fuel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="fuel_types",
                        to="exchange_rates.fuel_types",
                    ),
                ),
            ],
            options={
                "verbose_name": "Fuel",
                "verbose_name_plural": "Fuel",
            },
        ),
        migrations.CreateModel(
            name="Currency_Prices",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("buy_market_price", models.FloatField(blank=True, null=True)),
                ("sell_market_price", models.FloatField(blank=True, null=True)),
                ("change_market", models.CharField(max_length=64)),
                ("buy_bank_price", models.FloatField(blank=True, null=True)),
                ("sell_bank_price", models.FloatField(blank=True, null=True)),
                ("change_bank", models.CharField(max_length=64)),
                (
                    "currency",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="currency_currency_prices",
                        to="exchange_rates.currency",
                    ),
                ),
                (
                    "exchange_currency",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="exchange_currency_currency_prices",
                        to="exchange_rates.currency",
                    ),
                ),
            ],
            options={
                "verbose_name": "Currency_Prices",
                "verbose_name_plural": "Currencies_Prices",
            },
        ),
    ]

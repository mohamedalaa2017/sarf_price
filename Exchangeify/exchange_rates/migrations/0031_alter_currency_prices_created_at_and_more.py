# Generated by Django 4.2.7 on 2023-12-09 02:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("exchange_rates", "0030_alter_currency_prices_created_at_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="currency_prices",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 12, 9, 4, 14, 30, 560272)
            ),
        ),
        migrations.AlterField(
            model_name="fuel",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 12, 9, 4, 14, 30, 563271)
            ),
        ),
        migrations.AlterField(
            model_name="gold",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 12, 9, 4, 14, 30, 562271)
            ),
        ),
    ]

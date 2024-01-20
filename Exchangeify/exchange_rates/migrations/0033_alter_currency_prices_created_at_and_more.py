# Generated by Django 4.2.7 on 2023-12-09 02:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("exchange_rates", "0032_alter_currency_prices_created_at_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="currency_prices",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 12, 9, 4, 57, 54, 183613)
            ),
        ),
        migrations.AlterField(
            model_name="fuel",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 12, 9, 4, 57, 54, 187620)
            ),
        ),
        migrations.AlterField(
            model_name="gold",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 12, 9, 4, 57, 54, 185620)
            ),
        ),
    ]

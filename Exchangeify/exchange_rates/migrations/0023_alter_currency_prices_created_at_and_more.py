# Generated by Django 4.2.7 on 2023-12-09 00:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("exchange_rates", "0022_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="currency_prices",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 12, 9, 2, 43, 14, 504531)
            ),
        ),
        migrations.AlterField(
            model_name="fuel",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 12, 9, 2, 43, 14, 504531)
            ),
        ),
        migrations.AlterField(
            model_name="gold",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 12, 9, 2, 43, 14, 504531)
            ),
        ),
    ]

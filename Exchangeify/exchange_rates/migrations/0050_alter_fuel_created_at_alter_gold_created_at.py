# Generated by Django 4.2.7 on 2023-12-26 05:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("exchange_rates", "0049_alter_fuel_created_at_alter_gold_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fuel",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 12, 26, 7, 14, 31, 752026)
            ),
        ),
        migrations.AlterField(
            model_name="gold",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 12, 26, 7, 14, 31, 750026)
            ),
        ),
    ]

# Generated by Django 4.2.7 on 2023-12-26 04:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("exchange_rates", "0046_alter_fuel_created_at_alter_gold_created_at_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fuel",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 12, 26, 6, 55, 1, 84049)
            ),
        ),
        migrations.AlterField(
            model_name="gold",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 12, 26, 6, 55, 1, 83047)
            ),
        ),
    ]

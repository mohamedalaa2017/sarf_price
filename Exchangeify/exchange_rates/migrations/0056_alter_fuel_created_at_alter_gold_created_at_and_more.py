# Generated by Django 4.2.7 on 2023-12-27 02:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("exchange_rates", "0055_alter_fuel_created_at_alter_gold_created_at_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fuel",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 12, 27, 4, 25, 5, 957148)
            ),
        ),
        migrations.AlterField(
            model_name="gold",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 12, 27, 4, 25, 5, 955149)
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 12, 27, 4, 25, 5, 957148)
            ),
        ),
    ]

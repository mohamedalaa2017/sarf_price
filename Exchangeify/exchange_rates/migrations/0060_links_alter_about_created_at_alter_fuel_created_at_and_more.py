# Generated by Django 4.2.7 on 2023-12-28 05:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("exchange_rates", "0059_about_privacy_policy_terms_conditions_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Links",
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
                ("facebook", models.CharField(max_length=1000)),
                ("telegram", models.CharField(max_length=1000)),
                ("contact_us_email", models.CharField(max_length=1000)),
                (
                    "created_at",
                    models.DateTimeField(
                        default=datetime.datetime(2023, 12, 28, 7, 14, 44, 171957)
                    ),
                ),
            ],
            options={
                "verbose_name": "Privacy_Policy",
                "verbose_name_plural": "Privacy_Policy",
            },
        ),
        migrations.AlterField(
            model_name="about",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 12, 28, 7, 14, 44, 167958)
            ),
        ),
        migrations.AlterField(
            model_name="fuel",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 12, 28, 7, 14, 44, 165959)
            ),
        ),
        migrations.AlterField(
            model_name="gold",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 12, 28, 7, 14, 44, 162959)
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 12, 28, 7, 14, 44, 166959)
            ),
        ),
        migrations.AlterField(
            model_name="privacy_policy",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 12, 28, 7, 14, 44, 170961)
            ),
        ),
        migrations.AlterField(
            model_name="terms_conditions",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 12, 28, 7, 14, 44, 168959)
            ),
        ),
    ]

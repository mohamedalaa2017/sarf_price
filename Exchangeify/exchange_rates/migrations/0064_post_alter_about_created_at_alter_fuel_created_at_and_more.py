# Generated by Django 4.2.7 on 2024-01-17 14:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("exchange_rates", "0063_delete_post_alter_about_created_at_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("title", models.CharField(max_length=200)),
                ("image", models.ImageField(upload_to="20%y/%m/%d")),
                ("content", models.TextField()),
                ("meta_description", models.TextField()),
                (
                    "created_at",
                    models.DateTimeField(
                        default=datetime.datetime(2024, 1, 17, 16, 42, 56, 896680)
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="about",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 1, 17, 16, 42, 56, 897682)
            ),
        ),
        migrations.AlterField(
            model_name="fuel",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 1, 17, 16, 42, 56, 895683)
            ),
        ),
        migrations.AlterField(
            model_name="gold",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 1, 17, 16, 42, 56, 893685)
            ),
        ),
        migrations.AlterField(
            model_name="links",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 1, 17, 16, 42, 56, 899682)
            ),
        ),
        migrations.AlterField(
            model_name="privacy_policy",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 1, 17, 16, 42, 56, 898680)
            ),
        ),
        migrations.AlterField(
            model_name="terms_conditions",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 1, 17, 16, 42, 56, 897682)
            ),
        ),
    ]

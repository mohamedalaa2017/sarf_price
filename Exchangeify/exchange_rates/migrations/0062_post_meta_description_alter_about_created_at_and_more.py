# Generated by Django 4.2.7 on 2024-01-17 14:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("exchange_rates", "0061_metadetails_alter_links_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="meta_description",
            field=models.TextField(
                default=datetime.datetime(
                    2024, 1, 17, 14, 26, 13, 922117, tzinfo=datetime.timezone.utc
                )
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="about",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 1, 17, 16, 25, 5, 782382)
            ),
        ),
        migrations.AlterField(
            model_name="fuel",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 1, 17, 16, 25, 5, 780381)
            ),
        ),
        migrations.AlterField(
            model_name="gold",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 1, 17, 16, 25, 5, 779381)
            ),
        ),
        migrations.AlterField(
            model_name="links",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 1, 17, 16, 25, 5, 784380)
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 1, 17, 16, 25, 5, 781590)
            ),
        ),
        migrations.AlterField(
            model_name="privacy_policy",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 1, 17, 16, 25, 5, 784380)
            ),
        ),
        migrations.AlterField(
            model_name="terms_conditions",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 1, 17, 16, 25, 5, 783380)
            ),
        ),
    ]

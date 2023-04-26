# Generated by Django 4.2 on 2023-04-16 12:03

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Counties_2021",
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
                ("county", models.CharField(max_length=30)),
                ("county_id", models.IntegerField()),
                ("homicide", models.IntegerField()),
                ("robbery", models.IntegerField()),
                ("breakings", models.IntegerField()),
                ("stock_thef", models.IntegerField()),
                ("stealing", models.IntegerField()),
                ("vehicle_th", models.IntegerField()),
                ("d_drugs", models.IntegerField()),
                ("economic_c", models.IntegerField()),
                ("corruption", models.IntegerField()),
                ("population", models.IntegerField()),
                ("crimes", models.IntegerField()),
                ("crime_inde", models.IntegerField()),
                (
                    "geom",
                    django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326),
                ),
            ],
        ),
    ]

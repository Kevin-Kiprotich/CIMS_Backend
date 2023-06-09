# Generated by Django 4.2 on 2023-04-16 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shapes", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="counties_2021",
            name="breakings",
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name="counties_2021",
            name="corruption",
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name="counties_2021",
            name="county",
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name="counties_2021",
            name="crime_inde",
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name="counties_2021", name="crimes", field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name="counties_2021",
            name="economic_c",
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name="counties_2021", name="homicide", field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name="counties_2021",
            name="population",
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name="counties_2021", name="robbery", field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name="counties_2021", name="stealing", field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name="counties_2021",
            name="stock_thef",
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name="counties_2021",
            name="vehicle_th",
            field=models.BigIntegerField(),
        ),
    ]

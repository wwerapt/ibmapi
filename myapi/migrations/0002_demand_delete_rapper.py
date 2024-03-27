# Generated by Django 5.0.3 on 2024-03-26 14:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapi", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Demand",
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
                ("day", models.CharField(max_length=100)),
                ("branch", models.CharField(max_length=60)),
                ("demand_A", models.IntegerField()),
                ("demand_B", models.IntegerField()),
                ("demand_C", models.IntegerField()),
                ("demand_D", models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name="Rapper",
        ),
    ]

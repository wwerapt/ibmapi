# Generated by Django 5.0.3 on 2024-03-28 02:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "myapi",
            "0004_rename_demand_value_demandbranch_demand_product_a_value_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="demandbranch",
            name="demand_product_A_value",
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="demandbranch",
            name="demand_product_B_value",
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="demandbranch",
            name="demand_product_C_value",
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="demandbranch",
            name="demand_product_D_value",
            field=models.IntegerField(null=True),
        ),
    ]

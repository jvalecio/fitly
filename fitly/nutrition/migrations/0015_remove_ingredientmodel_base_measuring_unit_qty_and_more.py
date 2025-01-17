# Generated by Django 5.1.5 on 2025-01-16 13:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nutrition", "0014_remove_ingredientmodel_base_measuring_unit_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ingredientmodel",
            name="base_measuring_unit_qty",
        ),
        migrations.RemoveField(
            model_name="ingredientunitmodel",
            name="base_measuring_unit",
        ),
        migrations.RemoveField(
            model_name="ingredientunitmodel",
            name="base_unit_multiplier",
        ),
        migrations.AddField(
            model_name="ingredientmodel",
            name="base_measuring_unit",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="base_measuring_unit",
                to="nutrition.measuringunitmodel",
            ),
            preserve_default=False,
        ),
    ]

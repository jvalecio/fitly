# Generated by Django 5.1.5 on 2025-01-16 13:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nutrition", "0012_remove_recipemodel_ingredient_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="recipeitemmodel",
            name="recipe_item_measuring_unit",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.PROTECT,
                to="nutrition.measuringunitmodel",
            ),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name="ingredientmodel",
            name="measuring_units",
        ),
        migrations.AlterField(
            model_name="recipeitemmodel",
            name="ingredient",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="nutrition.ingredientmodel",
            ),
        ),
        migrations.AddField(
            model_name="ingredientmodel",
            name="measuring_units",
            field=models.ManyToManyField(to="nutrition.measuringunitmodel"),
        ),
    ]

# Generated by Django 5.1.5 on 2025-01-16 14:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nutrition", "0018_remove_recipemodel_recipe_item_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ingredientmodel",
            name="measuring_unit",
        ),
        migrations.AddField(
            model_name="ingredientunitmodel",
            name="ingredient",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                to="nutrition.ingredientmodel",
            ),
            preserve_default=False,
        ),
    ]

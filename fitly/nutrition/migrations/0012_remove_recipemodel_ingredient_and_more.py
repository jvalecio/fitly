# Generated by Django 5.1.5 on 2025-01-16 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nutrition", "0011_remove_recipemodel_ingredient_recipemodel_ingredient"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="recipemodel",
            name="ingredient",
        ),
        migrations.AddField(
            model_name="recipemodel",
            name="recipe_item",
            field=models.ManyToManyField(
                to="nutrition.recipeitemmodel", verbose_name="recipe_item"
            ),
        ),
    ]

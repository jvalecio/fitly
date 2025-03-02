# Generated by Django 5.1.5 on 2025-01-15 20:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nutrition", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="IngredientModel",
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
                ("source", models.CharField(max_length=100, unique=True)),
                ("base_measuring_unit", models.CharField(max_length=20)),
                (
                    "base_measuring_unit_qty",
                    models.FloatField(verbose_name="base_measuring_unity_quantity"),
                ),
                (
                    "calories",
                    models.DecimalField(
                        decimal_places=2, max_digits=4, verbose_name="calories"
                    ),
                ),
                (
                    "protein",
                    models.DecimalField(
                        decimal_places=2, max_digits=4, verbose_name="proein"
                    ),
                ),
                (
                    "carbohydrate",
                    models.DecimalField(
                        decimal_places=2, max_digits=4, verbose_name="carbohydrate"
                    ),
                ),
                (
                    "total_fat",
                    models.DecimalField(
                        decimal_places=2, max_digits=4, verbose_name="total_fat"
                    ),
                ),
                (
                    "saturated_fat",
                    models.DecimalField(
                        decimal_places=2, max_digits=4, verbose_name="saturated_fat"
                    ),
                ),
                (
                    "trans_fat",
                    models.DecimalField(
                        decimal_places=2, max_digits=4, verbose_name="trans_fat"
                    ),
                ),
                (
                    "cholesterol",
                    models.DecimalField(
                        decimal_places=2, max_digits=4, verbose_name="cholesterol"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MeasuringUnitModel",
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
                ("base_measuring_unit", models.CharField(max_length=20)),
                ("measuring_unit_name", models.CharField(max_length=20)),
                ("base_unit_multiplier", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="RecipeItemModel",
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
                (
                    "measuring_unit",
                    models.CharField(max_length=64, verbose_name="measuring_unit"),
                ),
                (
                    "measuring_unit_qty",
                    models.FloatField(verbose_name="measuring_unit_quantity"),
                ),
                (
                    "total_ingredient_calories",
                    models.DecimalField(
                        decimal_places=2, max_digits=4, verbose_name="calories"
                    ),
                ),
                (
                    "total_ingredient_protein",
                    models.DecimalField(
                        decimal_places=2, max_digits=4, verbose_name="proein"
                    ),
                ),
                (
                    "total_ingredient_carbohydrate",
                    models.DecimalField(
                        decimal_places=2, max_digits=4, verbose_name="carbohydrate"
                    ),
                ),
                (
                    "total_ingredient_total_fat",
                    models.DecimalField(
                        decimal_places=2, max_digits=4, verbose_name="total_fat"
                    ),
                ),
                (
                    "total_ingredient_saturated_fat",
                    models.DecimalField(
                        decimal_places=2, max_digits=4, verbose_name="saturated_fat"
                    ),
                ),
                (
                    "total_ingredient_trans_fat",
                    models.DecimalField(
                        decimal_places=2, max_digits=4, verbose_name="trans_fat"
                    ),
                ),
                (
                    "total_ingredient_cholesterol",
                    models.DecimalField(
                        decimal_places=2, max_digits=4, verbose_name="cholesterol"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RecipeModel",
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
                ("name", models.CharField(max_length=100, unique=True)),
                ("source", models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name="Ingredient",
        ),
        migrations.DeleteModel(
            name="Recipe",
        ),
        migrations.DeleteModel(
            name="RecipeItem",
        ),
        migrations.AddField(
            model_name="ingredientmodel",
            name="measuring_units",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="nutrition.measuringunitmodel",
            ),
        ),
        migrations.AddField(
            model_name="recipeitemmodel",
            name="ingredient",
            field=models.ManyToManyField(to="nutrition.ingredientmodel"),
        ),
        migrations.AddField(
            model_name="recipemodel",
            name="ingredient",
            field=models.ManyToManyField(to="nutrition.recipeitemmodel"),
        ),
    ]

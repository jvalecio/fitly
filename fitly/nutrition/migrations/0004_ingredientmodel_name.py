# Generated by Django 5.1.5 on 2025-01-15 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nutrition", "0003_remove_recipeitemmodel_ingredient_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="ingredientmodel",
            name="name",
            field=models.CharField(default=0, max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
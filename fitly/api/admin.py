from django.contrib import admin
from fitly.nutrition.models import IngredientModel, RecipeModel, MeasuringUnitModel, RecipeItemModel, IngredientUnitModel, MealPlanModel

admin.site.register(IngredientModel)
admin.site.register(RecipeModel)
admin.site.register(MeasuringUnitModel)
admin.site.register(RecipeItemModel)
admin.site.register(IngredientUnitModel)
admin.site.register(MealPlanModel)
# Register your models here.

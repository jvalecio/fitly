from django.contrib import admin
from fitly.nutrition.models import IngredientModel, RecipeModel, MeasuringUnitModel, RecipeItemModel

admin.site.register(IngredientModel)
admin.site.register(RecipeModel)
admin.site.register(MeasuringUnitModel)
admin.site.register(RecipeItemModel)
# Register your models here.

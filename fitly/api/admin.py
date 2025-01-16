from django.contrib import admin
from fitly.nutrition.models import IngredientModel, RecipeModel, MeasuringUnitModel, RecipeItemModel, IngredientUnitModel

admin.site.register(IngredientModel)
admin.site.register(RecipeModel)
admin.site.register(MeasuringUnitModel)
admin.site.register(RecipeItemModel)
admin.site.register(IngredientUnitModel)
# Register your models here.

from django.db import models
from django.utils.translation import gettext as _

class MeasuringUnitModel(models.Model):
    base_measuring_unit = models.CharField(max_length=20)
    measuring_unit_name = models.CharField(max_length=20)
    base_unit_multiplier = models.FloatField()

class IngredientModel(models.Model):
    name = models.CharField(unique=True, max_length=100)
    source = models.CharField(max_length=100)

    #ingredient_types = models.TextChoices("ingredient_type", "fruit", "vegetable")
    #ingredient_type = models.CharField(blank=True, choices = ingredient_types, max_length=100)

    base_measuring_unit = models.CharField(max_length=20)
    base_measuring_unit_qty = models.FloatField(verbose_name=_('base_measuring_unity_quantity'))
    
    measuring_units = models.ForeignKey(MeasuringUnitModel, on_delete=models.CASCADE)
    
    calories = models.DecimalField(verbose_name=_('calories'), decimal_places=2, max_digits=4)
    protein = models.DecimalField(verbose_name='proein', decimal_places=2, max_digits=4)
    carbohydrate = models.DecimalField(verbose_name='carbohydrate', decimal_places=2, max_digits=4)
    total_fat = models.DecimalField(verbose_name='total_fat', decimal_places=2, max_digits=4)
    saturated_fat = models.DecimalField(verbose_name='saturated_fat', decimal_places=2, max_digits=4)
    trans_fat = models.DecimalField(verbose_name='trans_fat', decimal_places=2, max_digits=4)
    cholesterol = models.DecimalField(verbose_name='cholesterol', decimal_places=2, max_digits=4)

class RecipeItemModel(models.Model):
    ingredient = models.ForeignKey(IngredientModel, on_delete=models.CASCADE)
    item_measuring_unit_qty = models.FloatField("measuring_unit_quantity")
    """
    total_ingredient_calories = models.DecimalField(blank=True,verbose_name='calories', decimal_places=2, max_digits=4)
    total_ingredient_protein = models.DecimalField(blank=True,verbose_name='proein', decimal_places=2, max_digits=4)
    total_ingredient_carbohydrate = models.DecimalField(blank=True,verbose_name='carbohydrate', decimal_places=2, max_digits=4)
    total_ingredient_total_fat = models.DecimalField(blank=True,verbose_name='total_fat', decimal_places=2, max_digits=4)
    total_ingredient_saturated_fat = models.DecimalField(blank=True,verbose_name='saturated_fat', decimal_places=2, max_digits=4)
    total_ingredient_trans_fat = models.DecimalField(blank=True,verbose_name='trans_fat', decimal_places=2, max_digits=4)
    total_ingredient_cholesterol = models.DecimalField(blank=True,verbose_name='cholesterol', decimal_places=2, max_digits=4, )
    """

    
class RecipeModel(models.Model):
    name = models.CharField(unique=True, max_length=100)
    source = models.CharField(unique=True, max_length=100)
    
    ingredient = models.ForeignKey(RecipeItemModel, on_delete=models.CASCADE)
# Create your models here.

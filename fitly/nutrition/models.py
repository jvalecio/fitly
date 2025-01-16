from django.db import models
from django.forms import model_to_dict
from django.utils.translation import gettext as _
from django.contrib.auth.models import User

class MeasuringUnitModel(models.Model):
    def __str__(self):
        return self.measuring_unit_name
    
    measuring_unit_name = models.CharField(unique=True, max_length=20)
    measuring_unit_abbreviation = models.CharField(unique=True, max_length=20)

class IngredientModel(models.Model):
    def __str__(self):
            return self.name
        
    name = models.CharField(unique=True, max_length=100)
    source = models.CharField(max_length=100)

    #ingredient_types = models.TextChoices("ingredient_type", "fruit", "vegetable")
    #ingredient_type = models.CharField(blank=True, choices = ingredient_types, max_length=100)

    base_measuring_unit = models.ForeignKey(MeasuringUnitModel, related_name="base_measuring_unit", on_delete=models.PROTECT)

    #base_measuring_unit_qty = models.FloatField(verbose_name=_('base_measuring_unity_quantity'))
    
    calories = models.DecimalField(verbose_name=_('calories'), decimal_places=2, max_digits=4)
    protein = models.DecimalField(verbose_name='protein', decimal_places=2, max_digits=4)
    carbohydrate = models.DecimalField(verbose_name='carbohydrate', decimal_places=2, max_digits=4)
    
    total_fat = models.DecimalField(verbose_name='total_fat', decimal_places=2, max_digits=4)
    saturated_fat = models.DecimalField(verbose_name='saturated_fat', decimal_places=2, max_digits=4)
    trans_fat = models.DecimalField(verbose_name='trans_fat', decimal_places=2, max_digits=4)
    cholesterol = models.DecimalField(verbose_name='cholesterol', decimal_places=2, max_digits=4)
    
    fiber = models.DecimalField(verbose_name='fiber', decimal_places=2, max_digits=4)

class IngredientUnitModel(models.Model):
    def __str__(self):
        return self.measuring_unit.measuring_unit_name
    
    ingredient = models.ForeignKey(IngredientModel, on_delete=models.CASCADE)
    
    measuring_unit = models.ForeignKey(MeasuringUnitModel, related_name="measuring_unit", on_delete=models.PROTECT)
    unit_multiplier = models.FloatField()
    
class RecipeModel(models.Model):
    def __str__(self):
         return self.name
     
    name = models.CharField(unique=True, max_length=100)
    source = models.CharField(max_length=100)
    
   # recipe_item = models.ManyToManyField(RecipeItemModel,name='recipe_item', verbose_name='recipe_item', )
    
class RecipeItemModel(models.Model):
    def __str__(self):
        return (self.ingredient.name + ";" + str(self.item_measuring_unit_qty) + ";" + self.recipe_item_measuring_unit.measuring_unit_name)
    
    recipe = models.ForeignKey(RecipeModel, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(IngredientModel, on_delete=models.PROTECT)
    
    item_measuring_unit_qty = models.FloatField("measuring_unit_quantity")
    recipe_item_measuring_unit = models.ForeignKey(IngredientUnitModel, on_delete=models.PROTECT)
    
    def compute_total_nutrients(self):
        multiplier = self.item_measuring_unit_qty * self.recipe_item_measuring_unit.unit_multiplier
        
        self.total_ingredient_calories = self.ingredient.calories * multiplier
        self.total_ingredient_protein = self.ingredient.protein * multiplier
        self.total_ingredient_carbohydrate = self.ingredient.carbohydrate * multiplier
        self.total_ingredient_total_fat = self.ingredient.total_fat * multiplier
        self.total_ingredient_saturated_fat = self.ingredient.saturated_fat * multiplier
        self.total_ingredient_trans_fat = self.ingredient.trans_fat * multiplier
        self.total_ingredient_cholesterol = self.ingredient.cholesterol * multiplier
    
    def save(self, *args, force_insert=False, force_update=False, using=None, update_fields=None):
        return super(RecipeItemModel, self).save(*args, force_insert=False, force_update=False, using=using, update_fields=update_fields)
    
class MealPlanModel(models.Model):
    def __str__(self):
        return self.name
    
    creation_date = models.DateField()
    start_date = models.DateField()
    end_date = models.DateField()
    
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=126)
    user = models.ForeignKey(User, models.CASCADE)
    
    target_calories = models.DecimalField(decimal_places=2, max_digits=4)
    target_protein = models.DecimalField(decimal_places=2, max_digits=4)
    target_carbohydrate = models.DecimalField(decimal_places=2, max_digits=4)
    target_total_fat = models.DecimalField(decimal_places=2, max_digits=4)
    target_fiber = models.DecimalField(decimal_places=2, max_digits=4) 
    
class MealItemModel(models.Model):
    def __str__(self):
        return self.name
    meal_plan = models.ForeignKey(MealPlanModel, on_delete=models.CASCADE)
    
    name = models.CharField(max_length=32)
    meal_time = models.DateField()
    
    recipe = models.ManyToManyField(RecipeModel)
    raw_ingredient = models.ManyToManyField(IngredientModel, null=True, blank=True)
    
    notes = models.CharField(max_length=128)

# Create your models here.

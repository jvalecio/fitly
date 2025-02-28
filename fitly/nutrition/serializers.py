from rest_framework.serializers import ModelSerializer

from .models import IngredientModel, MealPlanModel, RecipeModel, MeasuringUnitModel

class IngredientSerializer(ModelSerializer):
    def test_model_fields(self):
        pass
    class Meta:
        model = IngredientModel
        fields = (
            'name','source','base_measuring_unit','calories', 'protein', 'carbohydrate',
            'total_fat', 'saturated_fat', 'trans_fat',
            'cholesterol', 'fiber',
        )
        
class MealPlanSerializer(ModelSerializer):
    class Meta:
        model = MealPlanModel
        fields = (
            
        )
        
class RecipeSerializer(ModelSerializer):
    class Meta:
        model = RecipeModel
        fields = (
            
        )
        
class MeasuringUnitSerializer(ModelSerializer):
    class Meta:
        model = MeasuringUnitModel
        fields = (
            
        )      
       
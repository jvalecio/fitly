from rest_framework.serializers import ModelSerializer

from .models import IngredientModel

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
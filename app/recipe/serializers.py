from rest_framework import serializers
from coresapp.models import Tag, Ingredient


class TagSerializer(serializers.ModelSerializer):
    """serializer for tag objects"""

    class Meta:
        model = Tag
        fields = '__all__'
        read_only_fields = ('id',)


class IngredientSerializer(serializers.ModelSerializer):
    """serializer for Ingredient objects"""

    class Meta:
        model = Ingredient
        fields = ('id', 'name')
        read_only_fields = ('id',)
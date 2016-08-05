from rest_framework import serializers
from .models import Cupcake

class CupcakeSerializer(serializers.ModelSerializer):
    writer = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
     )
    class Meta:
        model = Cupcake
        fields = ('name', 'rating', 'price', 'image', 'writer','createdAt')

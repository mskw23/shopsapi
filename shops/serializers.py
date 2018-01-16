from rest_framework.serializers import ModelSerializer

from shops.models import Shop

class ShopListSerializer(ModelSerializer):
    class Meta:
        model = Shop
        fields = [
            'title',
            'slug',
            'description'
        ]

class ShopDetailSerializer(ModelSerializer):
    class Meta:
        model = Shop
        fields = [
            'title',
            'slug',
            'description'
        ]
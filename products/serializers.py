from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField

from products.models import Product

class ProductSerializer(ModelSerializer):
    image = SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'description',
            'shop'
        ]

    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image

class ProductCreateSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'shop',
            'image'
        ]

class ProductUpdateSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'title',
            'description'
        ]
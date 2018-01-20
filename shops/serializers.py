from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField

from shops.models import Shop

from comments.serializers import CommentSerializer
from comments.models import Comment

from products.serializers import ProductSerializer
from products.models import Product


class ShopListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='shops-api:detail',
        lookup_field='slug'
    )
    image = SerializerMethodField()
    class Meta:
        model = Shop
        fields = [
            'title',
            'image',
            'url',
            'slug'
        ]

    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image


class ShopDetailSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='shops-api:detail',
        lookup_field='slug'
    )
    user = SerializerMethodField()
    image = SerializerMethodField()
    comments = SerializerMethodField()
    products = SerializerMethodField()

    class Meta:
        model = Shop
        fields = [
            'id',
            'user',
            'title',
            'slug',
            'description',
            'image',
            'url',
            'comments',
            'products'
        ]

    def get_user(self, obj):
        return str(obj.user.username)

    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image

    def get_comments(self, obj):
        qs = Comment.objects.filter(shop=obj.id)
        comments = CommentSerializer(qs, many=True).data
        return comments

    def get_products(self, obj):
        qs = Product.objects.filter(shop=obj.id)
        products = ProductSerializer(qs, many=True).data
        return products


class ShopCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Shop
        fields = [
            'title',
            'description',
            'image'
        ]
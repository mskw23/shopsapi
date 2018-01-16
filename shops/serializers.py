from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField

from shops.models import Shop


class ShopListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='shops_api:detail',
        lookup_field='slug'
    )

    class Meta:
        model = Shop
        fields = [
            'id',
            'url',
            'title',
            'slug',
            'description'
        ]


class ShopDetailSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='shops_api:detail',
        lookup_field='slug'
    )
    user = SerializerMethodField()
    image = SerializerMethodField()
    class Meta:
        model = Shop
        fields = [
            'id',
            'user',
            'title',
            'slug',
            'description'
        ]

    def get_user(self, obj):
        return str(obj.user.username)

    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image


class ShopCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Shop
        fields = [
            'title',
            'description'
        ]
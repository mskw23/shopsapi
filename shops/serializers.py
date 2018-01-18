from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField

from shops.models import Shop

from comments.serializers import CommentSerializer
from comments.models import Comment


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
    comments = SerializerMethodField()
    products = SerializerMethodField()

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

    def get_comments(self, obj):
        content_type = obj.get_content_type
        comments = Comment.objects.fi


class ShopCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Shop
        fields = [
            'title',
            'description',
        ]
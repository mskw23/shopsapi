from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField, ImageField

from shops.models import Shop, create_slug

from comments.serializers import CommentSerializer
from comments.models import Comment

from products.serializers import ProductSerializer
from products.models import Product


class Base64ImageField(ImageField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.

    Heavily based on
    https://github.com/tomchristie/django-rest-framework/pull/1268

    Updated for Django REST framework 3.
    """

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension


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
    image = Base64ImageField(
        max_length=None, use_url=True,
    )

    class Meta:
        model = Shop
        fields = [
            'title',
            'description',
            'image',
            'slug',
            'id'
        ]

        extra_kwargs = {"slug": {"read_only": True},
                        "id": {"read_only": True}}

    def create(self, validated_data):
        title = validated_data['title']
        description = validated_data['description']
        image = validated_data['image']
        user = validated_data['user']
        shop_obj = Shop(
            title=title,
            description=description,
            image=image,
            user=user
        )
        #shop_obj.set_password(password)

        shop_obj.save()
        validated_data['slug'] = shop_obj.slug
        validated_data['id'] = shop_obj.id
        return validated_data
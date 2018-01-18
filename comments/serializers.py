from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField

from comments.models import Comment

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id',
            'title',
            'message',
            'user',
            'shop'
        ]

class CommentCreateSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'title',
            'message',
            'shop'
        ]

class CommentUpdateSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'title',
            'message'
        ]
from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField

from comments.models import Comment

class CommentSerializer(ModelSerializer):
    user = SerializerMethodField()
    class Meta:
        model = Comment
        fields = [
            'id',
            'title',
            'message',
            'user',
            'shop'
        ]
        
    def get_user(self, obj):
        return str(obj.user.username)

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
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.db.models import Q

from rest_framework.serializers import (
    CharField,
    EmailField,
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError
    )
from rest_framework_jwt.settings import api_settings

User = get_user_model()

class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [

        ]

class UserCreateSerializer(ModelSerializer):
    email = EmailField(label='Email')
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
        ]
        extra_kwargs = {"password":
                            {"write_only": True}}

    def validate(self, data):
        # email = data['email']
        # user_qs = User.objects.filter(email=email)
        # if user_qs.exists():
        #     raise ValidationError("This user has already registered.")
        return data

    def validate_email(self, value):
        data = self.get_initial()
        email = data.get('email')
        user_qs = User.objects.filter(email=email)
        if user_qs.exists():
            raise ValidationError("This user has already registered.")
        return value

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(
            username=username,
            email=email
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data

class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    #username = CharField()
    email = EmailField(label='Email Address')

    class Meta:
        model = User
        fields = [
            'email',
            'password',
            'token',

        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                        }

    def validate(self, data):
        user_obj = None
        email = data['email']
        password = data['password']
        user = User.objects.filter(Q(email=email)).distinct()
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("This email is not valid")

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Incorrect credentials, please try again")

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user_obj)
        token = jwt_encode_handler(payload)
        data['token'] = token

        return data

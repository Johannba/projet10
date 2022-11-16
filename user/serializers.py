


from rest_framework import serializers
from user .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "password",
            "username",
        )
        extra_kwargs = {
            "password": {"write_only": True, "style": {"input_type": "password"}}
        }

    def create(self, validated_data):
        return User.objects.create_user(
            validated_data["username"],
            password=validated_data["password"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"],
        )
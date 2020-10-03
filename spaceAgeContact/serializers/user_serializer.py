from rest_framework import serializers
from spaceAgeContact.models.user import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'students': {'required': False},
                        'workers': {'required': False},
                        'followings': {'required': False},
                        'follower': {'required': False}}

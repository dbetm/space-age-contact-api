from rest_framework import serializers
from spaceAgeContact.models.game import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'
        extra_kwargs = {'player': {'required': False}}

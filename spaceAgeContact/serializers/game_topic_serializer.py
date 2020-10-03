from rest_framework import serializers
from spaceAgeContact.models.game_topic import GameTopic


class GameTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameTopic
        fields = '__all__'

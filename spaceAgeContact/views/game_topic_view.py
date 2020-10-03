from rest_framework import viewsets
from spaceAgeContact.models.game_topic import GameTopic
from spaceAgeContact.serializers.game_topic_serializer import GameTopicSerializer


class GameTopicViewSet(viewsets.ModelViewSet):
    """
    Get all game_topics
    """
    queryset = GameTopic.objects.all()
    serializer_class = GameTopicSerializer
from rest_framework import viewsets
from spaceAgeContact.models.game import Game
from spaceAgeContact.serializers.game_serializer import GameSerializer


class GameViewSet(viewsets.ModelViewSet):
    """
    Get all games
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer
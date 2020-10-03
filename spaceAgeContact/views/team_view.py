from rest_framework import viewsets
from spaceAgeContact.models.team import Team
from spaceAgeContact.serializers.team_serializer import TeamSerializer


class TeamViewSet(viewsets.ModelViewSet):
    """
    Get all teams
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

from rest_framework import serializers
from spaceAgeContact.models.team import Team


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

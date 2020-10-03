from rest_framework import serializers
from spaceAgeContact.models.school import School


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'

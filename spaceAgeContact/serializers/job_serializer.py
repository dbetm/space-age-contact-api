from rest_framework import serializers
from spaceAgeContact.models.job import Job


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'

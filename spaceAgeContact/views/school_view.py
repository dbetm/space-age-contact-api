from rest_framework import viewsets
from spaceAgeContact.models.school import School
from spaceAgeContact.serializers.school_serializer import SchoolSerializer


class SchoolViewSet(viewsets.ModelViewSet):
    """
    Get all schools
    """
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
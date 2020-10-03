from rest_framework import viewsets
from spaceAgeContact.models.job import Job
from spaceAgeContact.serializers.job_serializer import JobSerializer


class JobViewSet(viewsets.ModelViewSet):
    """
    Get all jobs
    """
    queryset = Job.objects.all()
    serializer_class = JobSerializer

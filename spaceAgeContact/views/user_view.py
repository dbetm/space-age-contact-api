from rest_framework import viewsets
from spaceAgeContact.models.user import User
from spaceAgeContact.serializers.user_serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    Get all users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

from rest_framework import viewsets
from rest_framework.response import Response
from spaceAgeContact.models.user import User
from rest_framework.authtoken.models import Token
from rest_framework import status
from spaceAgeContact.serializers.user_serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    Get all users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        token, created = Token.objects.get_or_create(
            user=request.user_id)
        return Response({'token': token.key}, status=status.HTTP_201_CREATED, headers=headers)

from .models import Users
from .serializers import UserSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status

class ListCreateUser(ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

class RetrieveUpdateDestroyUser(RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    lookup_url_kwarg = "cpf"
    def get_object(self):
        lookup_value = self.kwargs.get(self.lookup_url_kwarg)
        queryset = self.get_queryset()
        try:

            user = queryset.get(cpf=lookup_value)
            return user
        except Users.DoesNotExist:
            raise Users.DoesNotExist("Usuário inexistente", status.HTTP_404_NOT_FOUND)

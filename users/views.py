from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from .models import CustomUser
from .serializers import CustomUserSerializer


class CustomUserModelViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]


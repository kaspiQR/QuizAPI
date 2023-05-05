from rest_framework.viewsets import ModelViewSet

from .models import QuizUser
from .serializers import QuizUserSerializer


class QuizUserModelViewSet(ModelViewSet):
    queryset = QuizUser.objects.all()
    serializer_class = QuizUserSerializer




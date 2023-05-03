from rest_framework.routers import DefaultRouter

from .models import Answer
from .views import QuizModelViewSet, QuestionModelViewSet, AnswerModelViewSet


router = DefaultRouter()

router.register('quiz', QuizModelViewSet)
router.register('question', QuestionModelViewSet)
router.register('answer', AnswerModelViewSet)

urlpatterns = router.urls


from rest_framework.routers import DefaultRouter

from .views import QuizUserModelViewSet

router = DefaultRouter()

router.register('quiz_user', QuizUserModelViewSet)


urlpatterns = router.urls

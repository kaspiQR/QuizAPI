from rest_framework.routers import DefaultRouter
from .views import CustomUserModelViewSet

router = DefaultRouter()

router.register('custom_user', CustomUserModelViewSet)

urlpatterns = router.urls

from rest_framework.routers import SimpleRouter
from .views import ContextViewSet

router = SimpleRouter()

router.register(r'context', ContextViewSet, basename="Context")
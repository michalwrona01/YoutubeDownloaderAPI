from rest_framework import routers
from .views import VideoViewSet, PlaylistViewSet

router = routers.DefaultRouter()
router.register(r'videos', VideoViewSet)
router.register(r'playlist', PlaylistViewSet)

from django.shortcuts import render
from .serializers import VideoSerializer, PlaylistSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Video, Playlist


class VideoViewSet(ModelViewSet):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()

class PlaylistViewSet(ModelViewSet):
    serializer_class = PlaylistSerializer
    queryset = Playlist.objects.all()

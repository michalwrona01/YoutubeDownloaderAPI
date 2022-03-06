from rest_framework import serializers
from .models import Video, Playlist


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'url_video_yt', 'user', 'playlist']


class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ['id', 'url_playlist_yt', 'user']

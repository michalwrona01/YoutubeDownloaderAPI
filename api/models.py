import pytube
from django.db import models
from django.contrib.auth import get_user_model
from pytube import YouTube
import pytube
from pytube.exceptions import VideoUnavailable


class Playlist(models.Model):
    url_playlist_yt = models.URLField(null=False, blank=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        playlist = pytube.Playlist(url=self.url_playlist_yt)
        return f'{playlist.title} - {self.user}'

    def save(self, *args, **kwargs):
        try:
            playlist = pytube.Playlist(url=self.url_playlist_yt)
        except VideoUnavailable:
            return
        else:
            super().save(*args, **kwargs)
            for video_url in playlist.video_urls:
                video = Video(url_video_yt=video_url, user=self.user, playlist=self)
                video.save()


class Video(models.Model):
    url_video_yt = models.URLField(null=False, blank=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE, null=True)

    def __str__(self):
        video_title = YouTube(url=self.url_video_yt).title
        return f'{video_title} - {self.user}'

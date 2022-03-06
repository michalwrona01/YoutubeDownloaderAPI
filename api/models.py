import pytube
from django.db import models
from django.contrib.auth import get_user_model
from pytube import YouTube
import pytube
from pytube.exceptions import VideoUnavailable


class Playlist(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    url_playlist_yt = models.URLField(null=True, blank=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        try:
            playlist = pytube.Playlist(url=self.url_playlist_yt)
        except VideoUnavailable:
            return
        else:
            if not self.title:
                self.title = playlist.title

            super(Playlist, self).save(*args, **kwargs)
            for video_url in playlist.video_urls:
                video = Video(url_video_yt=video_url, title=None, thumbnail_url=None, user=self.user, playlist=self)
                video.save()


class Video(models.Model):
    title = models.CharField(max_length=255, null=True, blank=False)
    url_video_yt = models.URLField(null=False, blank=False)
    thumbnail_url = models.URLField(null=False, blank=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        video = YouTube(url=self.url_video_yt)

        if not self.title:
            self.title = video.title
        if not self.thumbnail_url:
            self.thumbnail_url = video.thumbnail_url

        super(Video, self).save(*args, **kwargs)








from __future__ import unicode_literals

from django.db import models

class Album(models.Model):
    artist = models.CharField(max_length=100)
    album_title=models.CharField(max_length=200)
    genre = models.CharField(max_length=50)
    album_logo=models.CharField(max_length=200)

    def __str__(self):
        return self.album_title +' - '+self.artist

class song(models.Model):
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    file_type =models.CharField(max_length=10)
    song_title =models.CharField(max_length=200)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title
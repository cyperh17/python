#Difining models

from django.db import models

# Create your models here.

class Album(models.Model):
    artist = models.CharField(max_length=250) # creating table string field with max length 
    album_title = models.CharField(max_length=500) # creating table string field with max length
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

    # album1.song_set.create() # thats how we create new songs assosiated with this album
                               # using this way we dont need to set any refrences we just need to specify only value params

    def __str__(self):
        return 'Artist: {}, Title: {}'.format(self.artist, self.album_title)

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)

    def __str__(self):
        return self.song_title
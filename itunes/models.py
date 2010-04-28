from django.db import models

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist)
    
    def __unicode__(self):
        return self.title

class Track(models.Model):
    title = models.CharField(max_length=100)
    order_num = models.IntegerField(max_length=100)
    album = models.ForeignKey(Album)

    def __unicode__(self):
        return self.title

# Create your views here.
from django.views.generic.simple import direct_to_template
from keitai.itunes.models import *

def index(request):
    artists = Artist.objects.all().order_by('name')

    dictionary = {'artists':artists}
    return direct_to_template(request,'itunes/index.html',dictionary)

def artist(request,artist_id):
    albums = Album.objects.filter(artist__id=artist_id)
    artist = Artist.objects.get(pk=artist_id)
    dictionary = {'albums':albums, 'artist':artist}
    return direct_to_template(request,'itunes/artist.html',dictionary)

def album(request,artist_id,album_id):
    tracks = Track.objects.filter(album__id=album_id)
    album = Album.objects.filter(pk=album_id)
    artist = Artist.objects.get(pk=artist_id)
    dictionary = {'tracks':tracks, 'album':album,'artist':artist}
    return direct_to_template(request,'itunes/album.html',dictionary)

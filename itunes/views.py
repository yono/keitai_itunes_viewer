# Create your views here.
from django.views.generic.simple import direct_to_template
from keitai.itunes.models import *

class InitialArtists(object):

    def __init__(self,initial):
        self.initial = initial
        self.artists = []

def index(request):
    initials = Initial.objects.all().order_by('name')
    ias = []
    for initial in initials:
        ia = InitialArtists(initial)
        artists = Artist.objects.filter(initial=ia.initial)
        if len(artists) > 0:
            ia.artists = artists
            ias.append(ia)

    dictionary = {'initials':ias}
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

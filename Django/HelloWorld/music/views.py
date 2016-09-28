#Defining views

from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
#from django.template import loader
from music.models import Album, Song

# Create your views here.

def index(request):
    albums = Album.objects.all() # all data
    return render(request, 'music/index.html', { 'albums': albums })
    

def detail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist as e:
        raise Http404('Album does not exists')

    return render(request, 'music/detail.html', {'album_id': album_id, 'album': album.__str__() })
#Defining views

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
#from django.template import loader
from music.models import Album, Song

# Create your views here.

def index(request):
    albums = Album.objects.all() # all data
    return render(request, 'music/index.html', { 'all_albums': albums })
    

def detail(request, album_id):
    # try:
    #     album = Album.objects.get(pk=album_id)
    # except Album.DoesNotExist as e:
    #     raise Http404('Album does not exists')

    album = get_object_or_404(Album, pk=album_id)

    return render(request, 'music/detail.html', { 'album': album })

def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    selected_song_id = request.POST['song']

    try:
        song_db = album.song_set.get(pk=selected_song_id)
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {
            'album': album,
            'error_message': 'You did not selec a valid song'
        })
    else:
        song_db.is_favorite = True
        song_db.save()
        return render(request, 'music/detail.html', { 'album': album })
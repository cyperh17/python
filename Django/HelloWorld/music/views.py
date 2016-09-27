#Defining views

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from music.models import Album, Song

# Create your views here.

def index(request):
    albums = Album.objects.all() # all data
    template = loader.get_template('music/index.html') # loader already in template folder
    context = {
        'albums': albums
    }

    return HttpResponse(template.render(context, request))

    ##old
    # albums = Album.objects.all() # all data
    # html = '<h1>Music App Page</h1>'

    # html += '<ul>'

    # for album in albums:
    #     url = '/music/{}/'.format(album.id)
    #     html += '<li><a href="{}">{}</a></li>'.format(url, album.album_title)

    # html += '</ul>'
    # return HttpResponse(html)
    

def detail(request, album_id):
    album = Album.objects.filter(id=album_id)
    template = loader.get_template('music/detail.html') # loader already in template folder
    context = {
        'album_id': album_id,
        'album': album[0].__str__()
    }

    return HttpResponse(template.render(context, request))

    # title = '<h2>Details from Album id: {}</h2>'.format(album_id)
    # albums = Album.objects.filter(id=album_id)
    # result = ''

    # for a in albums:
    #     result += a.__str__()
    
    # result = title + result

    # result += '</br></br><a href="/music/">Return</a>'

    # return HttpResponse(result)
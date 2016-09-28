from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    url(r'^$', views.index, name='index'), # name - unique name for this url pattern

    # /music/1/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),

    # /music/1/favorite/
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
]
#Admin Section

from django.contrib import admin
from .models import Album, Song

# Register your models here.

admin.site.register(Album) # adding admin page to Album
admin.site.register(Song) # adding admin page to Song
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello world, you're at the socialists index")

def artist(request, artist_name):
    return HttpResponse("You're looking at artist: {0}".format(artist_name))

def gallery(request, gallery_name):
    return HttpResponse("You're looking at the gallery: {0}".format(gallery_name))

def event(request, event_name):
    return HttpResponse("You're looking at the event: {0}".format(event_name))
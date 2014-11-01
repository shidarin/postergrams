from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from socialists.models import Event

# Create your views here.


def index(request):
    latest_event_list = Event.objects.order_by('opening')[:5]
    template = loader.get_template('socialists/index.html')
    context = RequestContext(
        request,
        {
            'latest_event_list': latest_event_list,
        }
    )
    return HttpResponse(template.render(context))

def artist(request, artist_name):
    return HttpResponse("You're looking at artist: {0}".format(artist_name))

def gallery(request, gallery_name):
    return HttpResponse("You're looking at the gallery: {0}".format(gallery_name))

def event(request, event_name):
    return HttpResponse("You're looking at the event: {0}".format(event_name))
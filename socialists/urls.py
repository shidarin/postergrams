from django.conf.urls import patterns, url

from socialists import views

urlpatterns = patterns(
    '',
    # /socialists/
    url(r'^$', views.index, name='index'),
    # /socialists/artists/OllyMoss/
    url(r'^artists/(?P<artist_name>[\w\d]+)/$', views.artist, name='artist'),
    # /socialists/galleries/Mondo/
    url(r'^galleries/(?P<gallery_name>[\w\d]+)/$', views.gallery, name='gallery'),
    # /socialists/events/Batman75/
    url(r'^events/(?P<event_name>[\w\d]+)/$', views.event, name='event')
)
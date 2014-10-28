from django.conf.urls import patterns, include, url
from django.contrib import admin
from socialists import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'postergrams.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # /
    url(r'^$', views.index, name='index'),
    # /artists/OllyMoss/
    url(r'^artists/(?P<artist_name>[\w\d]+)/$', views.artist, name='artist'),
    # /galleries/Mondo/
    url(r'^galleries/(?P<gallery_name>[\w\d]+)/$', views.gallery, name='gallery'),
    # /events/Batman75/
    url(r'^events/(?P<event_name>[\w\d]+)/$', views.event, name='event'),
    # /admin/
    url(r'^admin/', include(admin.site.urls)),
)

admin.site.site_header = 'Postergrams administration'
admin.site.site_title = 'Postergrams site admin'

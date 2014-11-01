from django.contrib import admin
from socialists.models import Artist, Gallery, Event

class ArtistAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            None,
            {'fields': [
                'first_name',
                'middle_name',
                'last_name',
                'alias'
            ]}
        ),
        (
            'Social Media',
            {'fields': [
                'instagram',
                'twitter',
                'behance',
                'facebook',
                'website',
                'email'
            ]}
        )
    ]
    list_display = ('__unicode__', 'alias', 'instagram', 'twitter', 'email')
    search_fields = (
        'first_name', 'last_name',
        'alias', 'instagram', 'twitter', 'email'
    )


class GalleryAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            None,
            {'fields': [
                'name',
            ]}
        ),
        (
            'Location',
            {'fields': [
                'city',
                'address'
            ]}
        ),
        (
            'Social Media',
            {'fields': [
                'instagram',
                'twitter',
                'facebook',
                'website',
                'email'
            ]}
        )
    ]
    list_display = ('name', 'city', 'instagram', 'twitter', 'website')
    search_fields = ('name', 'city', 'instagram', 'twitter')


class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            None,
            {'fields': [
                'name',
                'host',
                'desc'
            ]}
        ),
        (
            'Dates & Times',
            {'fields': [
                'opening',
                'closing',
                'online_sale'
            ]}
        ),
        (
            'Artists',
            {'fields': [
                'artists',
            ]}
        )
    ]
    list_display = ('name', 'host_name', 'city', 'opening', 'is_current')
    list_filter = ('opening', )
    search_fields = ('name', )

admin.site.register(Artist, ArtistAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Event, EventAdmin)

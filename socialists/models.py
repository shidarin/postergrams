import datetime

from django.db import models


# =============================================================================
# MODELS
# =============================================================================

class SocialMedia(models.Model):
    """Model which contains all supported social media"""

    instagram = models.CharField(
        'Instagram',
        max_length=30,
        blank=True,
        default='',
        help_text='Instagram username, not url'
    )
    twitter = models.CharField(
        'Twitter',
        max_length=15,
        blank=True,
        default='',
        help_text='Twitter username, not url'
    )
    behance = models.CharField(
        'Behance',
        max_length=64,
        blank=True,
        default='',
        help_text='Behance username, not url'
    )
    facebook = models.CharField(
        'Facebook',
        max_length=51,
        blank=True,
        default='',
        help_text='Facebook username, not url'
    )
    website = models.URLField(
        'Website',
        blank=True,
        default='',
        help_text='Website. This should be a url'
    )
    email = models.EmailField(
        'Email',
        blank=True,
        default='',
        help_text='Email address'
    )

    class Meta:
        abstract = True

class Artist(SocialMedia):
    """Main Model for the Artist entries

    This model stores all the information needed to identify a specific artist.

    """
    may_be_blank = 'May be blank if artist only goes by their {0}'
    names = may_be_blank.format('alias')
    aliases = may_be_blank.format('real name')

    first_name = models.CharField(
        'First Name',
        max_length='64',
        blank=True,
        default='',
        help_text=names
    )
    middle_name = models.CharField(
        'Middle Name',
        max_length='64',
        blank=True,
        default='',
        help_text=names
    )
    last_name = models.CharField(
        'Last Name',
        max_length='64',
        blank=True,
        default='',
        help_text=names
    )
    alias = models.CharField(
        'Alias',
        max_length='128',
        blank=True,
        default='',
        help_text=aliases
    )

    def get_name(self):
        """Returns name in the 'last name, first middle' format"""
        if not self.has_name():
            return None

        name = '{last}{comma_space}{first}{first_middle_space}{middle}'
        return name.format(
            last=self.last_name if self.last_name else '',
            comma_space=', ' if self.last_name and (self.first_name or self.middle_name) else '',
            first=self.first_name if self.first_name else '',
            first_middle_space=' ' if self.first_name and self.middle_name else '',
            middle=self.middle_name if self.middle_name else '',
        ).title()

    def has_name(self):
        """True if Artist has any part of a name"""
        if self.first_name or self.middle_name or self.last_name:
            return True
        else:
            return False

    def has_alias(self):
        """True if Artist has an alias"""
        return True if self.alias else False

    def __unicode__(self):
        if self.has_alias() and self.has_name():
            alias = ' ({0})'.format(self.alias).title()
        elif self.has_alias():
            alias = self.alias.title()
        else:
            alias = ''

        return u'{name}{alias}'.format(
            name=self.get_name() if self.has_name() else '',
            alias=alias
        )


class Gallery(SocialMedia):
    """Gallery, website or group that hosts shows consisting of artists"""
    name = models.CharField(
        'Name',
        max_length=128,
        help_text='Name of the gallery, website or group'
    )
    address = models.TextField(
        'Physical Address',
        max_length=512,
        default='',
        blank=True,
        help_text='Actual real world physical address, if any'
    )


class Event(models.Model):
    """An art event of some kind"""
    name = models.CharField(
        'Event Name',
        max_length=64,
        default='',
        help_text='Name of the event'
    )
    host = models.ForeignKey(Gallery)
    desc = models.TextField(
        'Description',
        max_length=512,
        default='',
        blank=True,
        help_text='Short description of the event'
    )
    opening = models.DateTimeField(
        'Opening',
        help_text='Day and time of the event opening reception. If no '
                  'reception, just put midnight.'
    )
    closing = models.DateTimeField(
        'Closing',
        help_text='Day and time of the event closing reception. If no '
                  'reception, just put midnight.'
    )
    online_sale = models.DateTimeField(
        'Online Sale',
        blank=True,
        null=True,
        help_text='If prints will be available online at a certain day and '
                  'time, indicate that here.'
    )
    artists = models.ManyToManyField(
        Artist,
        blank=True,
        null=True,
        help_text='Select all artists currently known to be involved in the '
                  'event.'
    )


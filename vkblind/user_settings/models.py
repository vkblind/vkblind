
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class UserSettings(models.Model):
    user = models.OneToOneField(User, related_name='site_settings')
    font_size = models.CharField(max_length=5, choices=settings.FONT_SIZES, default=settings.FONT_SIZES[0][0])
    color_scheme = models.CharField(max_length=20, choices=settings.COLOR_SCHEMES, default=settings.COLOR_SCHEMES[0][0])

    def __unicode__(self):
        return '<UserSettings: user={username}, font_size={fsize} , color_scheme={color_scheme}>'.format(
            username=self.user.username,
            fsize=self.font_size,
            color_scheme=self.color_scheme,
        )

    class Meta:
        db_table = 'user_settings'

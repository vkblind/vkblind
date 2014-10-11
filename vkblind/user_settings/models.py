from django.db import models
from django.contrib.auth.models import User


class UserSettings(models.Model):
    user = models.ForeignKey(User)
    font_size = models.CharField(max_length=5, null=True, blank=True)
    color_scheme = models.CharField(max_length=20, null=True, blank=True)

    def __unicode__(self):
        return self.user.username

    class Meta:
        db_table = 'user_settings'

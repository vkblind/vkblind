from django.db import models
from django.contrib.auth.models import User

class Settings(models.Model):
    user = models.ForeignKey(User)
    font_size =  models.CharField(max_length=5,  null=True, blank=True)
    color_scheme = models.CharField(max_length=20,  null=True, blank=True)
    def __unicode__(self):
        return self.user.username + ": " + str(self.font_size) + " " + str(self.color_scheme)
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('user_settings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersettings',
            name='color_scheme',
            field=models.CharField(default=b'black', max_length=20, choices=[(b'black', b'black'), (b'white', b'white')]),
        ),
        migrations.AlterField(
            model_name='usersettings',
            name='font_size',
            field=models.CharField(default=b'L', max_length=5, choices=[(b'L', b'large'), (b'M', b'medium'), (b'S', b'small')]),
        ),
        migrations.AlterField(
            model_name='usersettings',
            name='user',
            field=models.OneToOneField(related_name=b'site_settings', to=settings.AUTH_USER_MODEL),
        ),
    ]

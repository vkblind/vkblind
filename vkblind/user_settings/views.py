# coding: utf-8

from annoying.decorators import render_to
from django.shortcuts import redirect
from . import models


@render_to('settings.html')
def settings(request):
    return {}


def save_settings(request):
    user_data = {
        'font_size': request.POST['font_size'],
        'color_scheme': request.POST['color_scheme'],
    }
    user_settings, created = models.UserSettings.objects.get_or_create(
        user=request.user, defaults=user_data)
    if not created:
        models.UserSettings.objects.filter(
            user=request.user).update(**user_data)
    return redirect('../')

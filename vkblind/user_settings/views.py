# coding: utf-8

from annoying.decorators import render_to
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.forms.models import model_to_dict

from .models import UserSettings
from .forms import UserSettingsForm


@render_to('settings.html')
def settings(request):
    """
    View user settings page with color/font-size options form
    """
    settings_inst, created = UserSettings.objects.get_or_create(user=request.user)
    return {
        'settings': model_to_dict(settings_inst)
    }


def save_settings(request):
    """
    Save user settings data from POST request
    """
    settings_inst, created = UserSettings.objects.get_or_create(user=request.user)

    form = UserSettingsForm(request.POST, instance=settings_inst)
    form.save()
    return redirect(reverse('settings'))

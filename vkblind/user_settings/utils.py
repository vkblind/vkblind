# coding: utf-8

from django.forms.models import model_to_dict

from .models import UserSettings
from .forms import UserSettingsForm


def get_user_settings(user):
    """
    Return user settings dict if user is authenticated or default settings for anonymous

    :type user: django.contrib.auth.models.User
    :rtype: dict
    """
    if user.is_authenticated():
        settings_inst, created = UserSettings.objects.get_or_create(user=user)
    else:
        settings_inst = UserSettings()

    user_params = {k:v for k,v in model_to_dict(settings_inst).items() if k in UserSettingsForm._meta.fields}

    return user_params

# coding: utf-8

from .user_settings.utils import get_user_settings


def user_settings(request):
    """
    Add user_settings dict to page
    """
    return {
        'user_settings': get_user_settings(request.user)
    }

# coding: utf-8
import logging
from functools import wraps

from django.contrib.auth.decorators import login_required

from .api import API

logger = logging.getLogger(__name__)


def vk_api(func):
    @login_required
    @wraps(func)
    def wrapper(*args, **kwgs):
        request = args[0]
        if request.user.is_authenticated and not hasattr(request, 'vk'):
            request.vk = API(access_token=request.user.social_auth.get().tokens)
        return func(*args, **kwgs)
    return wrapper

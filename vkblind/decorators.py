# -*- coding: utf-8 -*

import vk
from django.contrib.auth.decorators import login_required


def vk_api(func):

    @login_required
    def wrapper(*args, **kwgs):
        request = args[0]
        if request.user.is_authenticated and not hasattr(request, 'vk'):
            request.vk = vk.API(
                access_token=request.user.social_auth.get().tokens)
        return func(*args, **kwgs)

    return wrapper

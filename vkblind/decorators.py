# -*- coding: utf-8 -*

import vk


def vk_api(func):
    def wrapper(*args, **kwgs):
        request = args[0]
        if request.user.is_authenticated and not hasattr(request, 'vk'):
            request.vk = vk.API(
                access_token=request.user.social_auth.get().tokens)
        return func(*args, **kwgs)
    return wrapper

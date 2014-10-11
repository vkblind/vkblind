# -*- coding: utf-8 -*

import vk
from django.contrib.auth.decorators import login_required

from functools import wraps


def retry_on_exception(exception, times=10):
    def decorator(func):
        @wraps(func)
        def decorated(*args, **kwargs):
            for i in xrange(times):
                try:
                    return func(*args, **kwargs)
                except exception as e:
                    print "[{0}/{1}] Caught {2}".format(i + 1, times, e)
                    pass
        return decorated
    return decorator


def vk_api(func):
    @login_required
    @wraps(func)
    def wrapper(*args, **kwgs):
        request = args[0]
        if request.user.is_authenticated and not hasattr(request, 'vk'):
            request.vk = vk.API(
                access_token=request.user.social_auth.get().tokens)
        return func(*args, **kwgs)

    return wrapper

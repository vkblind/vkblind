# -*- coding: utf-8 -*
import time
import vk
from vk.api import APISession
from django.contrib.auth.decorators import login_required

from functools import wraps


def retry_on_exception(exception, times=10, sleep=None):
    def decorator(func):
        @wraps(func)
        def decorated(*args, **kwargs):
            err = Exception
            for i in xrange(times):
                try:
                    return func(*args, **kwargs)
                except exception as err:
                    # print "[{0}/{1}] Caught {2}".format(i + 1, times, e)
                    if sleep:
                        time.sleep(sleep)
            raise err
        return decorated
    return decorator


class API(APISession):
    @retry_on_exception(vk.VkAPIMethodError, times=5, sleep=0.4)
    def __call__(self, method_name, **method_kwargs):
        return super(API, self).__call__(method_name, **method_kwargs)


def vk_api(func):
    @login_required
    @wraps(func)
    def wrapper(*args, **kwgs):
        request = args[0]
        if request.user.is_authenticated and not hasattr(request, 'vk'):
            request.vk = API(
                access_token=request.user.social_auth.get().tokens)
        return func(*args, **kwgs)
    return wrapper

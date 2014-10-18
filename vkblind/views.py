# coding: utf-8

import vk
import logging
from pprintpp import pprint

from django.http import HttpResponseBadRequest
from django.contrib.auth import logout as logout_user
from django.shortcuts import redirect
from annoying.decorators import render_to

from .decorators import vk_api
from .utils import user_to_uid

logger = logging.getLogger(__name__)


@vk_api
@render_to('index.html')
def index(request):
    raise NotImplementedError


@render_to('accounts/login.html')
def login(request):
    return {}


@vk_api
@render_to('profile.html')
def profile(request, vkuser):
    """
    User profile view
    """
    try:
        account_data = request.vk.user_profile_data(vkuser)
    except vk.VkAPIMethodError as exc:
        logger.exception(repr(exc))
        return HttpResponseBadRequest('An error occurred, sorry')

    return {
        'account': account_data,
    }


def logout(request):
    logout_user(request)
    return redirect('/')


@render_to('help_page.html')
def help_page(request):
    return {}

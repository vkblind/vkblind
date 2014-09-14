# coding: utf-8

from annoying.decorators import render_to
from django.core.cache import cache
from django.contrib.auth import logout as logout_user
from django.contrib.auth.decorators import login_required
from django.shortcuts import resolve_url, redirect


@login_required
@render_to('index.html')
def index(request):
    try:
        import pprintpp
        import vk
        vkapi = vk.API(access_token=request.user.social_auth.get().tokens)

        groups = vkapi.groups.get()
        pprintpp.pprint(groups)

        wall = vkapi.wall.get(owner_id=-groups['items'][3])
        pprintpp.pprint(wall)
    except:
        pass
    return {}


@render_to('accounts/login.html')
def login(request):
    return {}


def logout(request):
    logout_user(request)
    return redirect(resolve_url('home'))

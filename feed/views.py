# coding: utf-8

from annoying.decorators import render_to
from django.core.cache import cache
from django.contrib.auth import logout as logout_user
from django.contrib.auth.decorators import login_required
from django.shortcuts import resolve_url, redirect
import time
from vkblind.decorators import vk_api


@vk_api
@render_to('feed.html')
def view_feed(request):
    owners = []
    items = []

    groups = request.vk.groups.get()

    # groups should be negative
    owners.extend(map(lambda x: x * -1, groups['items']))

    # extend items
    for owner_id in owners[:2]:
        wall = request.vk.wall.get(owner_id=owner_id)
        items.extend(wall['items'])
        time.sleep(0.2)

    return {
        'items': items
    }

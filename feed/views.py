# coding: utf-8

import time
from annoying.decorators import render_to
from vkblind.decorators import vk_api
from vkblind.utils import prepare_item_list


@vk_api
@render_to('feed.html')
def view_feed(request):
    owners = []
    items = []

    # extend owners list by user groups
    # group ids should be negative
    groups = request.vk.groups.get()
    owners.extend(map(lambda x: x * -1, groups['items']))

    # extend owners list by user friends
    friends = request.vk.friends.get()
    owners.extend(friends['items'])

    # get posts by owner
    for owner_id in owners[:10]:
        wall = request.vk.wall.get(
            owner_id=owner_id,
        )
        items.extend(wall['items'])
        time.sleep(0.2)

    # prepare items for display
    items = prepare_item_list(request.vk, items)

    return {
        'items': items,
        'debug_mode': request.REQUEST.get('debug') == '1',
    }

# coding: utf-8

import time

from annoying.decorators import render_to
from vkblind.decorators import vk_api, retry_on_exception
from vkblind.utils import prepare_item_list

from requests.exceptions import ReadTimeout


@retry_on_exception(ReadTimeout)
@vk_api
@render_to('feed.html')
def view_feed(request):
    owners = [request.vk.users.get()[0]['id']]
    items = []

    # extend owners list by user groups
    # group ids should be negative
    groups = request.vk.groups.get()
    if groups['count']:
        owners.extend(map(lambda x: x * -1, groups['items']))

    # extend owners list by user friends
    friends = request.vk.friends.get(order='hints', fields='last_seen')
    if friends['count']:
        friends = filter(lambda friend: not 'deactivated' in friend,
                         friends['items'])
        friends.sort(key=lambda x: -x['last_seen']['time'])
        owners.extend(map(lambda x: x['id'], friends))

    # get posts by owner
    for owner_id in owners[:40]:
        wall = request.vk.wall.get(
            owner_id=owner_id,
        )
        items.extend(wall['items'])

    # prepare items for display
    items = prepare_item_list(request.vk, items)

    return {
        'items': items,
        'debug_mode': request.REQUEST.get('debug') == '1',
    }

# -*- coding: utf-8 -*


from annoying.decorators import render_to

from vkblind.decorators import vk_api
from vkblind.utils import get_owner, prepare_item_list


@vk_api
@render_to('view_groups.html')
def view_groups(request):
    """
    """
    groups_info = request.vk.groups.get()
    group_ids_str = ','.join(map(lambda x: str(x), groups_info['items']))
    groups = request.vk.groups.getById(group_ids=group_ids_str)
    return {'groups': groups}


@vk_api
@render_to('view_group.html')
def view_group(request, group_id):
    group_id = '-{0}'.format(group_id)
    group = get_owner(request.vk, group_id)
    wall = request.vk.wall.get(owner_id=group_id)
    items = prepare_item_list(request.vk, wall['items'])

    return {
        'group': group,
        'items': items,
        'titles': True,
        'debug_mode': request.REQUEST.get('debug') == '1',
    }

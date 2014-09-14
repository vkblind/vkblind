# -*- coding: utf-8 -*


from annoying.decorators import render_to

from vkblind.decorators import vk_api


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
    group = request.vk.groups.getById(group_id=group_id)[0]
    wall = request.vk.wall.get(owner_id='-%s' % group_id)
    return {'group': group, 'wall_items': wall['items'][:100]}

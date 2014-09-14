# -*- coding: utf-8 -*

import vk
from annoying.decorators import render_to
from django.contrib.auth.decorators import login_required


@login_required
@render_to('view_groups.html')
def view_groups(request):
    """
    """
    vkapi = vk.API(access_token=request.user.social_auth.get().tokens)
    groups_info = vkapi.groups.get()
    group_ids_str = ','.join(map(lambda x: str(x), groups_info['items']))

    groups = vkapi.groups.getById(group_ids=group_ids_str)
    group_names = [group['name'] for group in groups]

    return {'group_names': group_names}

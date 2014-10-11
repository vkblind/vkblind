# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"

from annoying.decorators import render_to

from vkblind.decorators import vk_api


VK_HOST = "https://vk.com"
ITEMS_COUNT = 20

@vk_api
@render_to('search.html')
def search(request):
    vk_url = users = groups = None

    query = request.REQUEST.get('c[q]')
    if query:
        groups = request.vk.groups.search(q=query, count=ITEMS_COUNT)['items']
        users = request.vk.users.search(q=query, count=ITEMS_COUNT)['items']

        vk_url = VK_HOST + request.get_full_path()

    return {'groups': groups or [], 'users': users or [], 'vk_url': vk_url}

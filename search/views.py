# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"

from annoying.decorators import render_to

from vkblind.decorators import vk_api


@vk_api
@render_to('search.html')
def search(request):
    groups = None
    users = None

    if request.method == 'POST':
        query = request.POST.get('query')
        if query:
            groups = request.vk.groups.search(q=query, count=10)['items']
            users = request.vk.users.search(q=query, count=10)['items']

    return {'groups': groups or [], 'users': users or []}

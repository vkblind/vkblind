# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"

from annoying.decorators import render_to

from vkblind.decorators import vk_api


@vk_api
@render_to('search.html')
def search(request):
    if request.method == 'POST':
        query = request.POST['query']
        groups = request.vk.groups.search(q=query, count=10)['items']
        return {'groups': groups}
    else:
        return {'groups': []}

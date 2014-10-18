# -*- coding: utf-8 -*-

from annoying.decorators import render_to

from django.conf import settings
from django.http import HttpResponseBadRequest

from vkblind.decorators import vk_api


@vk_api
@render_to('search.html')
def search(request):
    """
    Search in news (aka statuses), users (aka people) and groups (aka communities)
    """
    query = request.REQUEST.get('q')
    if not query:
        return {
            "query": "",
            "section": "auto"
        }

    search_providers = {
        'communities': request.vk.groups,
        'people': request.vk.users,
        'statuses': request.vk.newsfeed
    }

    section = request.REQUEST.get('section', 'auto')
    if section == 'auto':
        sections_names = search_providers.keys()
    elif isinstance(section, basestring):
        sections_names = [section]
    elif isinstance(section, list):
        sections_names = [name for name in section if name in search_providers]
    else:
        return HttpResponseBadRequest('An error occurred, sorry')

    result = {
        "vk_url": settings.VK_HOST + request.get_full_path(),
        "query": query,
        "section": section
    }

    for section_name in sections_names:
        result[section_name] = search_providers[section_name].search(q=query, count=settings.ITEMS_LIMIT)['items']

    return result

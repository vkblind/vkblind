# coding: utf-8
import time
from django.core.cache import cache

OWNER_CACHE_KEY = 'owner_{0}'


def get_owner(vk, owner_id):
    """
    Return owner data from cache
    Otherwise get it from vk
    """
    owner_id = str(owner_id)
    key = OWNER_CACHE_KEY.format(owner_id)
    owner = cache.get(key)
    if owner is None:
        time.sleep(0.2)
        if owner_id.startswith('-'):
            owner = vk.groups.getById(group_id=[owner_id[1:]])
        else:
            owner = vk.users.get(user_ids=[owner_id])[0]
        if isinstance(owner, list):
            owner = owner[0]

        if not owner.get('name', None):
            owner['name'] = u'{first_name} {last_name}'.format(**owner)
        cache.set(key, owner, 86400)
    return owner
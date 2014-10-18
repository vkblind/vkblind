# coding: utf-8

import logging
from functools import wraps

from django.conf import settings
from django.core.cache import cache
from django.utils.translation import ugettext as _

OWNER_CACHE_KEY = 'owner_{0}'

logger = logging.getLogger(__name__)


def get_owner(vk, owner_id):
    """
    Return owner data from cache
    Otherwise get it from vk
    """
    owner_id = str(owner_id)
    key = OWNER_CACHE_KEY.format(owner_id)
    owner = cache.get(key)
    if owner is None:
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


def prepare_item_list(vk, items):
    """
    Sort, slice and prepare items
    """
    items.sort(key=lambda x: x['date'], reverse=True)
    items = items[:30]
    items = filter(lambda x: bool(x['text'].strip()), items)
    for item in items:
        item['owner'] = get_owner(vk, item['owner_id'])
    return items


# TODO: здесь нужна интернационализация и склонятор
MONTHS_LIST = [
    u'января',
    u'февраля',
    u'марта',
    u'апреля',
    u'мая',
    u'июня',
    u'июля',
    u'августа',
    u'сентября',
    u'октября',
    u'ноября',
    u'декабря'
]


def detect_birth_date(bdate=None):
    """
    Return cleaned user birthdate.

    :type bdate: unicode | NoneType
    :param bdate: "bdate" field value from {vkapi.users.get} api call
    :rtype: unicode
    """
    if bdate is None:
        # birth date is hidden
        birth_date_str = _(u'Скрыта')

    elif bdate.count('.') == 1:
        # year is hidden
        bday, bmonth_str = bdate.split('.')
        bmonth = MONTHS_LIST[int(bmonth_str) - 1]
        birth_date_str = ' '.join([bday, bmonth])

    elif bdate.count('.') == 2:
        # full birth date
        bday, bmonth_str, byear_str = bdate.split('.')
        bmonth = MONTHS_LIST[int(bmonth_str) - 1]
        birth_date_str = ' '.join([bday, bmonth, byear_str, u' г.'])

    else:
        birth_date_str = _(u'Неизвестна')
        logger.error('vk api returned incorrect birth date: %s', bdate)

    return birth_date_str


def user_to_uid(vk_user):
    """
    Convert vk_user identifier to uid int

    :type vk_user: basestring
    :rtype: int
    """
    return int(vk_user.lstrip('id'))


def retry_on_exception(exception, times=10, sleep=None):
    def decorator(func):
        @wraps(func)
        def decorated(*args, **kwargs):
            err = Exception
            for i in xrange(times):
                try:
                    return func(*args, **kwargs)
                except exception as exc:
                    logger.exception(repr(exc))
                    if sleep:
                        time.sleep(sleep)
            raise err
        return decorated
    return decorator

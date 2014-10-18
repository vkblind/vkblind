# coding: utf-8
"""
VK.API wrapper
"""

import vk
import time
import logging
from functools import wraps
from vk.api import APISession

from django.conf import settings

from .utils import detect_birth_date, retry_on_exception


logger = logging.getLogger(__name__)


class API(APISession):
    """
    VK.API wrapper
    """
    @retry_on_exception(vk.VkAPIMethodError, times=5, sleep=0.4)
    def __call__(self, method_name, **method_kwargs):
        return super(API, self).__call__(method_name, **method_kwargs)

    def user_profile_data(self, vk_user):
        """
        Return user profile data

        :type vk_user: basestring
        :param vk_user: vk user identifier
        :rtype: dict
        """

        # using {users.get} api call instead of {account.getProfileInfo} 'cause latter is Standalone-only

        found_accounts = self.users.get(user_ids=vk_user, fields=','.join(settings.VK_USER_FIELDS))

        if not len(found_accounts) or len(found_accounts) > 1:
            raise vk.VkAPIMethodError('something is wrong with user %s account', vk_user)

        account = found_accounts[0]

        birth_date = account.get('bdate', None)

        account['bdate'] = detect_birth_date(birth_date)

        return account

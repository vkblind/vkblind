# -*- coding: utf-8 -*-

__author__ = 'chipiga86@gmail.com'

import re
from string import punctuation

unreadable_pattern = r'[^\w\s%s]' % re.sub(r'(.)', r'\\\1', punctuation)
VK_INTERNAL_LINKS = re.compile(r'\[(id|club)(\d*?)\|(.*?)\]')


def strip_unreadable(text):
    return re.sub(unreadable_pattern, '', text, flags=re.U)


def process_vk_internal_links(text):
    """
    Преобразовывает линки вида [club123|Club name]
    """
    result = re.sub(VK_INTERNAL_LINKS, r'<a href="/\1/\2">\3</a>', text)
    return result

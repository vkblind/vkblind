# -*- coding: utf-8 -*-

__author__ = 'chipiga86@gmail.com'

import re
from string import punctuation

unreadable_pattern = r'[^\w\s%s]' % re.sub(r'(.)', r'\\\1', punctuation)
VK_INTERNAL_LINKS = re.compile(r'\[(id|club)(\d*?)\|(.*?)\]')
VK_TAGS = re.compile(r'#(\w+?)(?:\s|$|\.|,|!|\?)', re.U)


def strip_unreadable(text):
    return re.sub(unreadable_pattern, '', text, flags=re.U)


def process_vk_internal_links(text):
    """
    Преобразовывает линки вида [club123|Club name] и теги
    """
    result = re.sub(VK_INTERNAL_LINKS, r'<a href="/\1/\2">\3</a>', text)
    result = re.sub(VK_TAGS, r'<a href="/search?section=statuses&q=%23\1">#\1</a>', result)
    return result

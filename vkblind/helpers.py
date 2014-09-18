# -*- coding: utf-8 -*-

__author__ = 'chipiga86@gmail.com'

import re
from string import punctuation

unreadable_pattern = r'[^\w\s%s]' % re.sub(r'(.)', r'\\\1', punctuation)


def strip_unreadable(text):
    return re.sub(unreadable_pattern, '', text, flags=re.U)

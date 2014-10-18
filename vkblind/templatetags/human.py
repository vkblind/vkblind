# coding: utf-8

import datetime
import re
from string import punctuation
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from django.utils.html import urlize

import humanize
from django.template import Library

from vkblind.helpers import strip_unreadable, process_vk_internal_links

register = Library()


@register.filter
def human_datetime(date):
    date = datetime.datetime.fromtimestamp(date)
    return '{0}, {1}'.format(humanize.naturalday(date),
                             humanize.naturaltime(date))


@register.filter
def human_date(date):
    return humanize.naturalday(datetime.datetime.fromtimestamp(date))


@register.filter
def human_time(date):
    return humanize.naturaltime(datetime.datetime.fromtimestamp(date))


@register.filter(is_safe=True, needs_autoescape=True)
@stringfilter
def process_links(value, autoescape=None):
    """
    Convert vk internal [club123|Club name] links as well as external links
    into a clickable format and autoescape the rest of the text
    """
    return mark_safe(
        process_vk_internal_links(
            urlize(value, nofollow=True, autoescape=autoescape)
        )
    )

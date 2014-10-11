# coding: utf-8

import datetime
import re
from string import punctuation
from django.utils.safestring import mark_safe

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


@register.filter
def readable(text):
    # отрезаем лишние юникод-символы
    text = strip_unreadable(text)

    # преобразовываем линки вида [club123|Club name]
    text = process_vk_internal_links(text)

    return mark_safe(text)

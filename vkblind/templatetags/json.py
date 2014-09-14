# coding: utf-8
import simplejson
from django.template import Library
from django.utils.safestring import mark_safe

register = Library()



@register.filter
def as_json(data, indent=None):
    """Convert python dict to JSON on the fly"""
    return mark_safe(simplejson.dumps(data, bool(indent), indent))


@register.filter
def format_json(value):
    """Convert dict to a formatted JSON string"""
    return simplejson.dumps(value, sort_keys=True, indent=4, use_decimal=True)

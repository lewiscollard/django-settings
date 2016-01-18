from django import template

from ..utils import get_setting as get_setting_util

register = template.Library()


@register.simple_tag()
def setting(key):
    # Output the setting by key
    return get_setting_util(key, default=key)


@register.assignment_tag()
def get_setting(key, default=None):
    # Get the setting by key
    return get_setting_util(key, default)

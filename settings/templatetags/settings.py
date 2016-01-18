from django import template

from ..models import Setting

register = template.Library()


@register.simple_tag()
def setting(key):
    # Get the setting by key
    try:
        return Setting.objects.get(key=key).value()
    except Setting.DoesNotExist:
        return key


@register.assignment_tag()
def get_setting(key):
    # Get the setting by key
    try:
        return Setting.objects.get(key=key).value()
    except Setting.DoesNotExist:
        return None

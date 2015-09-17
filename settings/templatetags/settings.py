from django import template
from django.template.defaultfilters import linebreaksbr

from ..models import Setting

register = template.Library()


@register.simple_tag()
def get_setting(key):
    # Get the setting by key
    try:
        setting = Setting.objects.get(key=key)
        return {
            'string': setting.string,
            'text': linebreaksbr(setting.text),
            'number': setting.number,
            'image': setting.image.file.url if setting.image else '',
        }[setting.type]
    except Setting.DoesNotExist:
        return key

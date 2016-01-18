from .models import Setting


def get_setting(key, default=None):
    try:
        return Setting.objects.get(key=key).value()
    except Setting.DoesNotExist:
        return default

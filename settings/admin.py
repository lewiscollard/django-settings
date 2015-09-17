from django.conf import settings
from django.contrib import admin

from .models import Setting


class SettingAdmin(admin.ModelAdmin):
    prepopulated_fields = {'key': ['name']}

    def get_form(self, request, obj=None, **kwargs):
        if obj and request.user.username in settings.SETTINGS_ADMINS:
            self.exclude = ['name', 'key']
            self.prepopulated_fields = {}

        return super(SettingAdmin, self).get_form(request, obj, **kwargs)

    def has_add_permission(self, request):
        return request.user.username in settings.SETTINGS_ADMINS

    def has_delete_permission(self, request, obj=None):
        return request.user.username in settings.SETTINGS_ADMINS

    class Media:
        js = ("/static/settings/js/admin/fields.js",)


admin.site.register(Setting, SettingAdmin)

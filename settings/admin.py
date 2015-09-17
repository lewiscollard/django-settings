from django.contrib import admin
from camfed.apps.settings.models import Setting


class SettingAdmin(admin.ModelAdmin):
    prepopulated_fields = {'key': ['name']}

    def get_form(self, request, obj=None, **kwargs):
        if obj:
            if request.user.username != 'james':
                self.exclude = ['name', 'key']
                self.prepopulated_fields = {}

        return super(SettingAdmin, self).get_form(request, obj, **kwargs)

    def has_add_permission(self, request):
        if request.user.username == 'james':
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.username == 'james':
            return True
        return False

    class Media:
        js = ("/static/settings/js/admin/fields.js",)


admin.site.register(Setting, SettingAdmin)

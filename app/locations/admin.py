from django.contrib import admin
from .models import Location


class LocationAdmin(admin.ModelAdmin):
    list_display = ['user', 'latitude','longitude' ,'begin','end']
    search_fields = ('user',)

    def save_model(self, request, obj, form, change):
            obj.user = request.user
            super().save_model(request, obj, form, change)

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = ("user", )
        form = super(LocationAdmin, self).get_form(request, obj, **kwargs)
        return form

admin.site.register(Location, LocationAdmin)

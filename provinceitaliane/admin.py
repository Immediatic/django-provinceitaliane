from django.contrib import admin
from django.utils.translation import ugettext as _
from reversion.admin import VersionAdmin
from models import Province, Region

class ProvinceAdmin(VersionAdmin):
    list_display = ('coat_of_arms', 'name', 'code', 'region', 'capital')
    list_display_links = ('name', )
    #list_editable = ('region', )
    list_filter = ('region', 'capital')
    list_per_page = 10
    search_fields = ('name', 'region__name', 'code')

    def coat_of_arms(self, obj):
        if obj.coat:
            return "<img src='%s' width='20' alt='%s' />" % (obj.coat, obj.name)
        else:
            return "&nbsp;"
    coat_of_arms.allow_tags = True
    coat_of_arms.short_description = _('Coat')

admin.site.register(Province, ProvinceAdmin)

class RegionAdmin(VersionAdmin):
    list_display = ('coat_of_arms', 'name', 'position', 'special')
    list_display_links = ('name', )
    list_filter = ('position', 'special')
    list_per_page = 20
    search_fields = ('name', )

    def coat_of_arms(self, obj):
        if obj.coat:
            return "<img src='%s' width='20' alt='%s' />" % (obj.coat, obj.name)
        else:
            return "&nbsp;"
    coat_of_arms.allow_tags = True
    coat_of_arms.short_description = _('Coat')

admin.site.register(Region, RegionAdmin)
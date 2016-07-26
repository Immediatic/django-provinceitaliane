from django.contrib import admin
from django.utils.translation import ugettext as _
from provinceitaliane.models import Province, Region, District


class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name', 'province', 'prefix', 'cap', 'link')
    list_filter = ('province__region', )
    search_fields = ('name', 'province__code', 'cap', 'province__name')


class ProvinceAdmin(admin.ModelAdmin):
    list_display = ('coat_of_arms', 'name', 'code', 'region', 'capital')
    list_display_links = ('name', )
    list_filter = ('region', 'capital')
    list_per_page = 10
    search_fields = ('name', 'region__name', 'code')

    def coat_of_arms(self, obj):
        if obj.coat:
            return "<img src='%s' width='20' alt='%s' />" % (obj.coat, obj.name)
        else:
            return "&nbsp;"
    coat_of_arms.allow_tags = True
    coat_of_arms.short_description = _('coat')


class RegionAdmin(admin.ModelAdmin):
    list_display = ('coat_of_arms', 'name', 'position', 'special')
    list_display_links = ('name', )
    list_filter = ('position', 'special')
    list_per_page = 20
    search_fields = ('name', )
    prepopulated_fields = {'slug': ('name',)}

    def coat_of_arms(self, obj):
        if obj.coat:
            return "<img src='%s' width='20' alt='%s' />" % (obj.coat, obj.name)
        else:
            return "&nbsp;"
    coat_of_arms.allow_tags = True
    coat_of_arms.short_description = _('coat')


admin.site.register(District, DistrictAdmin)
admin.site.register(Province, ProvinceAdmin)
admin.site.register(Region, RegionAdmin)
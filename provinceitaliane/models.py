#coding=utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

region_position_list = (
    ('N', _('North')),
    ('C', _('Center')),
    ('S', _('South')),
    ('I', _('Islands')),
)


@python_2_unicode_compatible
class Region(models.Model):
    """
    Italian Regions
    References: http://it.wikipedia.org/wiki/Regioni_dell%27Italia
    """
    name = models.CharField(_('Name'), max_length=1000)
    slug = models.SlugField(_('Slug'), unique=True)
    position = models.CharField(_('Position'), max_length=1, choices=region_position_list)
    special = models.BooleanField(_('Special laws'), default=False)
    coat = models.URLField(_('Coat'), max_length=200, blank=True, null=True)

    class Meta:
        ordering = ('name', )
        verbose_name = _("Italian region")
        verbose_name_plural = _("Italian regions")

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Province(models.Model):
    code = models.CharField(_('Code'), max_length=2, unique=True)
    name = models.CharField(_('Name'), max_length=1000)
    region = models.ForeignKey(Region, verbose_name=_('Region'))
    capital = models.BooleanField(_('Capital'), default=False)
    coat = models.URLField(_('Coat'), max_length=200, blank=True, null=True)

    class Meta:
        ordering = ('code', )
        verbose_name = _("Italian province")
        verbose_name_plural = _("Italian provinces")

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class District(models.Model):
    name = models.CharField(_('Name'), max_length=1000)
    province = models.ForeignKey(Province, verbose_name=_('Province'))
    prefix = models.CharField(_('Prefix'), max_length=200)
    cap = models.CharField(_('CAP'), max_length=5)
    link = models.URLField(_('Link'), null=True, blank=True)

    class Meta:
        ordering = ('province', 'name')
        verbose_name = _("Italian district")
        verbose_name_plural = _("Italian districts")

    def __str__(self):
        return u"{0} ({1})".format(self.name, self.province.code)

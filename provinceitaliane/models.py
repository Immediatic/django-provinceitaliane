#coding=utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import AutoSlugField

region_position_list = (
    ('N', _('North')),
    ('C', _('Center')),
    ('S', _('South')),
    ('I', _('Islands')),
)

class Region(models.Model):
    """
    Italian Regions
    References: http://it.wikipedia.org/wiki/Regioni_dell%27Italia
    """
    name = models.CharField(_('name'), max_length=1000)
    slug = AutoSlugField(_('slug'), populate_from='name', unique=True, editable=False)
    position = models.CharField(_('position'), max_length=1, choices=region_position_list)
    special = models.BooleanField(_('special laws'), default=False)
    coat = models.URLField(_('coat'), verify_exists=True, max_length=200, blank=True, null=True)

    class Meta:
        ordering = ('name', )
        verbose_name = _("italian region")
        verbose_name_plural = _("italian regions")

    def __unicode__(self):
        return u'%s' % (self.name)

class Province(models.Model):
    code = models.CharField(_('code'), max_length=2, unique=True)
    name = models.CharField(_('name'), max_length=1000)
    region = models.ForeignKey(Region, verbose_name=_('region'))
    capital = models.BooleanField(_('capital'), default=False)
    coat = models.URLField(_('coat'), verify_exists=False, max_length=200, blank=True, null=True)

    class Meta:
        ordering = ('code', )
        verbose_name = _("italian province")
        verbose_name_plural = _("italian provinces")

    def __unicode__(self):
        return u'%s' % (self.name)

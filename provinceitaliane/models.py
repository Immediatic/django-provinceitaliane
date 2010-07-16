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
    name = models.CharField(_('Name'), max_length=1000)
    slug = AutoSlugField(_('Slug'), populate_from='name', unique=True, editable=False)
    position = models.CharField(_('Position'), max_length=1, choices=region_position_list)
    special = models.BooleanField(_('Special laws'), default=False)
    coat = models.URLField(_('Coat'), verify_exists=True, max_length=200, blank=True, null=True)

    class Meta:
        ordering = ('name', )
        verbose_name = _("Italian Region")
        verbose_name_plural = _("Italian Regions")

    def __unicode__(self):
        return u'%s' % (self.name)

class Province(models.Model):
    code = models.CharField(_('Code'), max_length=2, unique=True)
    name = models.CharField(_('Name'), max_length=1000)
    region = models.ForeignKey(Region, verbose_name=_('Region'))
    capital = models.BooleanField(_('Capital'), default=False)
    coat = models.URLField(_('Coat'), verify_exists=False, max_length=200, blank=True, null=True)

    class Meta:
        ordering = ('code', )
        verbose_name = _("Italian Province")
        verbose_name_plural = _("Italian Provinces")

    def __unicode__(self):
        return u'%s' % (self.name)

from django.db import models
from django.utils.translation import ugettext_lazy as _
from dj_mixin.publications.models import Publication


class Tariff(Publication):

    speed = models.CharField(
        verbose_name=_('tariff speed'),
        max_length=255,
    )
    title = models.CharField(
        verbose_name=_('tariff title'),
        max_length=255,
    )
    price = models.CharField(
        verbose_name=_('tariff price'),
        max_length=255,
    )
    content = models.TextField(
        verbose_name=_('tariff content'),
    )

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = _('tariff items')
        verbose_name = _('tariff')
        ordering = ['-weight', 'title']

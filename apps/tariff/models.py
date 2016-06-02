from django.db import models
from django.utils.translation import ugettext_lazy as _

from publications.models import Publication
from publications.managers import PublishedManager


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

    published = PublishedManager()

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = _('tariff items')
        verbose_name = _('tariff')
        ordering = ['-weight', 'title']


class ConnectRequest(models.Model):
    tariff = models.ForeignKey(
        Tariff,
        verbose_name=_('tariff'),
    )
    fio = models.CharField(
        verbose_name=_('user fio'),
        max_length=255,
    )
    contact = models.CharField(
        verbose_name=_('user contact'),
        max_length=255,
    )
    address = models.CharField(
        verbose_name=_('user address'),
        max_length=255,
    )
    answered = models.BooleanField(
        default=False,
        verbose_name=_('answered'),
    )
    create_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('create date'),
    )

    def __unicode__(self):
        return u'{0} {1}'.format(self.address, self.tariff.title);

    class Meta:
        verbose_name_plural = _('connect request items')
        verbose_name = _('connect request item')
        ordering = ['-create_date']
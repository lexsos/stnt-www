from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from publications.admin import PublicationAdmin
from admintinymce.admin import AdminTinymceMixin

from .models import Tariff, ConnectRequest


class TariffAdmin(AdminTinymceMixin, PublicationAdmin):
    list_filter = ('weight', 'enabled')
    list_display = ('title', 'weight', 'enabled')

    fieldsets = (
        (
            _('Tariff parameters'),
            {
                'classes': ('wide',),
                'fields': ('speed', 'title', 'price', 'content')
            }
        ),
    ) + PublicationAdmin.fieldsets

    rich_fields = ('content',)


class ConnectRequestAdmin(admin.ModelAdmin):
    list_filter = ('tariff', 'answered', 'create_date')
    list_display = ('create_date', 'tariff', 'fio', 'address', 'contact', 'answered')


admin.site.register(Tariff, TariffAdmin)
admin.site.register(ConnectRequest, ConnectRequestAdmin)

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from publications.admin import PublicationAdmin
from admintinymce.admin import AdminTinymceMixin

from .models import Tariff


class TafiffAdmin(AdminTinymceMixin, PublicationAdmin):
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


admin.site.register(Tariff, TafiffAdmin)

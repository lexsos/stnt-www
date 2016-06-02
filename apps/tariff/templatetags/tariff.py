from __future__ import absolute_import
from django import template
from django.conf import settings

from tariff.forms import ConnectRequestForm


register = template.Library()


@register.inclusion_tag('tariff/tag/connect_request_form.html')
def connect_request_form():
    return {
        'form': ConnectRequestForm(),
        'STATIC_URL': settings.STATIC_URL,
    }

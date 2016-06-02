from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import ConnectRequest, Tariff


class ConnectRequestForm(forms.ModelForm):
    fio = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': _('please, enter fio'),
                'class': 'form-control',
            }
        )
    )
    contact = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': _('please, enter contact'),
                'class': 'form-control',
            }
        )
    )
    address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': _('please, enter address'),
                'class': 'form-control',
            }
        )
    )
    tariff = forms.ModelChoiceField(
        empty_label=_('please, enter tariff'),
        queryset = Tariff.published,
        widget=forms.Select(
            attrs={
                'placeholder': _('please, enter tariff'),
                'class': 'form-control',
            }
        )
    )

    class Meta:
        model = ConnectRequest
        fields = ('tariff', 'fio', 'contact', 'address')
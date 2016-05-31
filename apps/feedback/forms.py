from django import forms
from django.utils.translation import ugettext_lazy as _
from captcha.fields import CaptchaField

from .models import Question


class QuestionForm(forms.ModelForm):

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
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': _('please, enter question'),
                'class': 'form-control',
                'rows': 3,
            }
        )
    )
    #captcha = CaptchaField()

    class Meta:
        model = Question
        fields = ('fio', 'contact', 'content')

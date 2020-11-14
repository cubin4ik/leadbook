from django import forms
from .models import Phone


class PhoneCreateForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = "__all__"
        labels = {
            'country_code': '',
            'area_code': '',
            'number': '',
            'extension': ''
        }
        help_texts = {
            'area_code': 'code.',
            'number': 'number',
            'extension': 'extension',
        }

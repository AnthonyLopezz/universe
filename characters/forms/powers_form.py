from django import forms
from characters.models import Powers


class Power_form(forms.ModelForm):
    class Meta:
        model = Powers
        fields = [
            'name'
        ]
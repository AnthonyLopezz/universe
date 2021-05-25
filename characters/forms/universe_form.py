from django import forms
from characters.models import Universe


class Universe_form(forms.ModelForm):
    class Meta:
        model = Universe
        fields = [
            'name',
            'date_foundation'
        ]

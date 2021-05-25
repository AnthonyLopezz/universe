from django import forms
from characters.models import Character


class Character_form(forms.ModelForm):
    class Meta:
        model = Character
        fields = [
            'universe',
            'name',
            'description',
            'image',
        ]

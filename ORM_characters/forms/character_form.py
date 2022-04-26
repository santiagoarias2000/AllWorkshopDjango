from django import forms
from ORM_characters.models import Character


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = [
            'name',
            'description',
            'image',
            'universe'
        ]
from django import forms
from ORM_characters.models import Powers_character, Powers


class Powers_characterForm(forms.ModelForm):
    class Meta:
        model = Powers_character
        fields = [
            'powers',
            'characters',
            'number'
        ]


class PowersForm(forms.ModelForm):
    class Meta:
        model = Powers
        fields = [
            'name'
        ]

from django import forms
from ORM_characters.models import Universe


class UniverseForm(forms.ModelForm):
    class Meta:
        model = Universe
        fields = [
            'name',
            'description',
            'date_foundation'
        ]


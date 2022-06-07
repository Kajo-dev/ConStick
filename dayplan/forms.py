from dataclasses import field
import imp
import django


from django import forms
from .models import Plans

class PlansFrom(forms.ModelForm):
    class Meta:
        model = Plans
        fields = [
            'zadanie',
            'data',
            'czas'
        ]

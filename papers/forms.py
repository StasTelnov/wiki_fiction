from django.forms import ModelForm
from .models import Paper
from django import forms


class PaperForm(ModelForm):
    class Meta:
        model = Paper
        fields = [
            'user',
            'tag',
            'title',
            'text',
            'rating',
        ]
        widgets = {'tag': forms.SelectMultiple(attrs={'class': 'chosen-select'})}


from django.forms import ModelForm
from .models import Paper
from django import forms


class PaperForm(ModelForm):
    class Meta:
        model = Paper
        fields = [
            'tags',
            'title',
            'text',
            'rating',
        ]
        widgets = {'tag': forms.SelectMultiple(attrs={'class': 'chosen-select', 'width': '170px'})}


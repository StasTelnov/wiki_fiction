from django.forms import ModelForm
from .models import Paper, Comment
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
        widgets = {'tags': forms.SelectMultiple(attrs={'class': 'chosen-select', 'id': 'tags'})}


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = [
            'text',
            'rating',
        ]

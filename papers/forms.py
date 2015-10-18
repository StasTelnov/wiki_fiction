from django import forms
from libs.fields import ChosenSelect
from .models import Paper, Comment


class PaperForm(forms.ModelForm):

    class Meta:
        model = Paper
        fields = [
            'tags',
            'title',
            'text',
        ]
        widgets = {
            'tags': ChosenSelect(
                attrs={'class': 'chosen-select', 'id': 'tags'}
            )
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = [
            'text',
            'rating',
        ]

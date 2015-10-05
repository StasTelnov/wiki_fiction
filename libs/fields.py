from django import forms


class ChosenSelect(forms.SelectMultiple):
    class Media:
        css = {
            'all': ('chosen/css/chosen.css',),
        }
        js = ('chosen/js/chosen.jquery.js', 'libs/chosen_init.js')


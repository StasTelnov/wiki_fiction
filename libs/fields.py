from django import forms


class ChosenSelect(forms.SelectMultiple):

    class Media:
        css = {
            "all": ("/static/bower_components/chosen/chosen.min.css",)
        }
        js = ("/static/bower_components/chosen/chosen.jquery.min.js",
              "libs/chosen_init.js")

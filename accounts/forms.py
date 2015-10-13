# from django.forms import ModelForm
from .models import MyUser
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _
from django import forms


class MyUserForm(UserCreationForm):

    class Meta:
        model = MyUser
        fields = ("username",)


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = MyUser
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "avatar",
        )

    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
        'password_incorrect': _("Your old password was entered incorrectly. "
                                "Please enter it again."),
    }
    new_password1 = forms.CharField(label=_("New password"),
                                    widget=forms.PasswordInput, required=False)
    new_password2 = forms.CharField(label=_("New password confirmation"),
                                    widget=forms.PasswordInput, required=False)

    old_password = forms.CharField(label=_("Old password"),
                                   widget=forms.PasswordInput)

    def clean_old_password(self):
        """
        Validates that the old_password field is correct.
        """
        old_password = self.cleaned_data["old_password"]
        if not self.instance.check_password(old_password):
            raise forms.ValidationError(
                self.error_messages['password_incorrect'],
                code='password_incorrect',
            )
        return old_password

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                )
        return password2

    def save(self, commit=True):
        super().save(commit=False)
        if self.cleaned_data['new_password1']:
            self.instance.set_password(self.cleaned_data['new_password1'])
        if commit:
            self.instance.save()
        return self.instance

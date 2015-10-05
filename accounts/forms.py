from django.forms import ModelForm
from .models import MyUser
from django.contrib.auth.forms import UserCreationForm


class MyUserForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ("username",)



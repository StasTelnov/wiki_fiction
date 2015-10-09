from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.utils.translation import ugettext_lazy as _

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, primary_key=True)
#     avatar = models.ImageField(upload_to='avatars', default='default-avatar.jpg')


class MyUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars')

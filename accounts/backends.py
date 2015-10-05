from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class EmailOrUsernameModelBackend(ModelBackend):
    """
    This is a ModelBacked that allows authentication with either a username or an email address.

    """
    def authenticate(self, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        if '@' in username:
            kwargs = {'email': username}
        else:
            kwargs = {'username': username}
        try:
            # user = UserModel.objects.get(**kwargs)
            users = UserModel.objects.filter(**kwargs)
            for user in users:
                if user.check_password(password):
                    return user
        except UserModel.DoesNotExist:
            return None

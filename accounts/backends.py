from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class EmailOrUsernameModelBackend(ModelBackend):

    """
    This is a ModelBacked that allows authentication with either a username
    or an email address.
    """

    def authenticate(self, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        if '@' in username:
            kwargs = {'email': username}
        else:
            kwargs = {'username': username}

        for user in UserModel.objects.filter(**kwargs):
            if user.check_password(password):
                return user
        else:
            return None

        # try:
        #     user = UserModel.objects.get(**kwargs)
        # except UserModel.DoesNotExist:
        #     return None

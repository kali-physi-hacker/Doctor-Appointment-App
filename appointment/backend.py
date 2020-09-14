from django.contrib.auth import get_user_model


User = get_user_model()


class EmailAuthBackend(object):
    """
    Authenticate user with email
    """
    def authenticate(self, request, username=None, password=None):
        """
        Implementing this method to make users authenticate using with emails
        :param request:
        :param username:
        :param password:
        :return:
        """
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        """
        Return a user with the specific user_id
        :param user_id:
        :return:
        """
        try:
            user = User.objects.get(pk=user_id)
            return user
        except User.DoesNotExist:
            return None

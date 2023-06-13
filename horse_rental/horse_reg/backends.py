from django.contrib.auth.backends import ModelBackend
from horse_reg.models import CustomUser


class EmailAuthBackends(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = CustomUser(email=username)
            if user.check_password(raw_password=password):
                user.is_active = True
                return user
        except CustomUser.DoesNotExist:
            pass

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            pass

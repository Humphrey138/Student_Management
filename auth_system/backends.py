# auth/backends.py
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from teachers.models import Teacher

User = get_user_model()

class CustomAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        if username is None or password is None:
            return None

        try:
            # Authenticate with the User model
            user = User.objects.get(username=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            # Authenticate with the Teacher model
            try:
                teacher = Teacher.objects.get(email=username)
                if teacher.user.check_password(password):
                    return teacher.user
            except Teacher.DoesNotExist:
                return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None